# importa a biblioteca socket (comunicação em rede)
import socket

# define o endereço do servidor (localhost = seu próprio computador)
HOST = '127.0.0.1'

# define a porta onde o servidor está escutando
PORT = 5000

# cria um socket TCP/IP
# AF_INET = IPv4
# SOCK_STREAM = protocolo TCP (conexão confiável)
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# conecta ao servidor usando host e porta
cliente.connect((HOST, PORT))

# pede o nome ao utilizador
nome = input("Digite o seu nome: ")

# envia o nome para o servidor
# encode() transforma string → bytes (obrigatório na rede)
cliente.send(nome.encode())

# recebe dados do servidor (até 1024 bytes)
# decode() transforma bytes → string
lista = cliente.recv(1024).decode()

# imprime título
print("\nItens disponíveis para votação:")

# imprime a lista recebida do servidor
print(lista)

# pede ao utilizador que escolha uma opção
voto = input("Escolha a opção: ")

# envia o voto para o servidor (convertido para bytes)
cliente.send(voto.encode())

# recebe a resposta final do servidor
resposta = cliente.recv(1024).decode()

# mostra a resposta do servidor
print("\nResposta do servidor:", resposta)

# fecha a conexão com o servidor
cliente.close()