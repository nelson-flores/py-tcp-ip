import socket
import json

# endereço do servidor (localhost)
HOST = '127.0.0.1'

# porta do servidor
PORT = 5000

# opções disponíveis para votação
opcoes = {
    "1": "Java",
    "2": "Python",
    "3": "C++"
}

# conjunto para guardar utilizadores que já votaram (evita duplicados)
utilizadores_que_ja_votaram = set()

# cria o socket TCP (IPv4 + TCP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# associa o socket ao endereço e porta
server.bind((HOST, PORT))

# coloca o servidor à escuta (até 5 conexões na fila)
server.listen(5)

print(f"Servidor à escuta em {HOST}:{PORT}")

# loop infinito (servidor sempre ativo)
while True:
    # aceita uma conexão de cliente
    conn, addr = server.accept()

    print(f"\nCliente ligado: {addr}")

    try:
        # RECEBER NOME DO UTILIZADOR

        # recebe até 1024 bytes, converte para string e remove espaços
        nome = conn.recv(1024).decode().strip()

        print(f"Utilizador recebido: {nome}")

        # ENVIAR LISTA DE OPÇÕES

        # cria uma string formatada com as opções
        lista = "\n".join([f"{k} - {v}" for k, v in opcoes.items()])

        # envia lista ao cliente (convertida para bytes)
        conn.send(lista.encode())

        # RECEBER VOTO DO CLIENTE

        voto = conn.recv(1024).decode().strip()

        print(f"Voto recebido: {voto}")

        # REGRA DE NEGÓCIO

        # verifica se o utilizador já votou
        if nome in utilizadores_que_ja_votaram:
            resposta = {
                "status": "erro",
                "mensagem": "Utilizador já votou"
            }

        # verifica se o voto é inválido
        elif voto not in opcoes:
            resposta = {
                "status": "erro",
                "mensagem": "Voto inválido"
            }

        # voto válido
        else:
            # adiciona utilizador ao conjunto
            utilizadores_que_ja_votaram.add(nome)

            resposta = {
                "status": "ok",
                "mensagem": "Voto confirmado",
                "linguagem": opcoes[voto]
            }

        # ENVIAR RESPOSTA AO CLIENTE

        # converte resposta para JSON (string) e depois para bytes
        conn.send(json.dumps(resposta).encode())

    except Exception as e:
        # caso ocorra erro, imprime no servidor
        print("Erro:", e)

    finally:
        # fecha conexão com o cliente (sempre)
        conn.close()
        print("Conexão encerrada.")