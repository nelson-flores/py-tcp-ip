import socket
import threading

HOST = "168.231.114.32"
PORT = 5000


def receber_mensagens(cliente):
    """Escuta mensagens do servidor."""
    while True:
        try:
            mensagem = cliente.recv(1024)
            if not mensagem:
                print("\n[INFO] Conexão encerrada pelo servidor.")
                break

            texto = mensagem.decode("utf-8")

            if texto == "NICK":
                cliente.send(apelido.encode("utf-8"))
            else:
                print(texto, end="")
        except (ConnectionResetError, ConnectionAbortedError, OSError):
            print("\n[INFO] Desconectado.")
            break


def enviar_mensagens(cliente):
    """Lê entrada do utilizador e envia ao servidor."""
    while True:
        try:
            mensagem = input()
            cliente.send(mensagem.encode("utf-8"))

            if mensagem.strip() == "/sair":
                try:
                    cliente.close()
                except OSError:
                    pass
                break
        except (EOFError, KeyboardInterrupt):
            try:
                cliente.send("/sair".encode("utf-8"))
                cliente.close()
            except OSError:
                pass
            break
        except OSError:
            break


if __name__ == "__main__":
    apelido = input("Digite seu nome/apelido: ").strip() or "Anónimo"

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORT))

    thread_receber = threading.Thread(target=receber_mensagens, args=(cliente,), daemon=True)
    thread_receber.start()

    enviar_mensagens(cliente)
