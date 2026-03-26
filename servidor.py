import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

clientes = []
apelidos = []
lock = threading.Lock()


def enviar_para_todos(mensagem: bytes, cliente_origem=None):
    """Envia a mensagem para todos os clientes conectados, exceto a origem."""
    with lock:
        clientes_atuais = list(clientes)

    for cliente in clientes_atuais:
        if cliente != cliente_origem:
            try:
                cliente.send(mensagem)
            except OSError:
                remover_cliente(cliente)


def remover_cliente(cliente):
    """Remove cliente e seu apelido das listas globais."""
    with lock:
        if cliente in clientes:
            indice = clientes.index(cliente)
            apelido = apelidos[indice]
            clientes.pop(indice)
            apelidos.pop(indice)
        else:
            return

    try:
        cliente.close()
    except OSError:
        pass

    aviso = f"[SERVIDOR] {apelido} saiu do chat.\n".encode("utf-8")
    print(aviso.decode("utf-8").strip())
    enviar_para_todos(aviso)


def lidar_com_cliente(cliente):
    """Recebe mensagens de um cliente e retransmite aos demais."""
    while True:
        try:
            mensagem = cliente.recv(1024)
            if not mensagem:
                remover_cliente(cliente)
                break

            texto = mensagem.decode("utf-8").strip()

            if texto == "/sair":
                remover_cliente(cliente)
                break

            with lock:
                if cliente not in clientes:
                    break
                indice = clientes.index(cliente)
                apelido = apelidos[indice]

            mensagem_formatada = f"{apelido}: {texto}\n".encode("utf-8")
            print(mensagem_formatada.decode("utf-8").strip())
            enviar_para_todos(mensagem_formatada, cliente_origem=cliente)

        except (ConnectionResetError, ConnectionAbortedError, OSError):
            remover_cliente(cliente)
            break


def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind((HOST, PORT))
    servidor.listen()

    print(f"Servidor de chat ouvindo em {HOST}:{PORT}")

    while True:
        cliente, endereco = servidor.accept()
        print(f"Nova conexão de {endereco[0]}:{endereco[1]}")

        cliente.send("NICK".encode("utf-8"))
        apelido = cliente.recv(1024).decode("utf-8").strip()

        with lock:
            clientes.append(cliente)
            apelidos.append(apelido)

        print(f"Apelido registrado: {apelido}")
        cliente.send("[SERVIDOR] Conectado com sucesso!\n".encode("utf-8"))
        enviar_para_todos(f"[SERVIDOR] {apelido} entrou no chat.\n".encode("utf-8"), cliente)

        thread = threading.Thread(target=lidar_com_cliente, args=(cliente,), daemon=True)
        thread.start()


if __name__ == "__main__":
    iniciar_servidor()
