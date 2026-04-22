import socket

HOST = "127.0.0.1"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"Servidor HTTP em execução em http://{HOST}:{PORT}")

while True:
    client_socket, client_address = server.accept()
    print(f"\nConexão recebida de {client_address}")

    request = client_socket.recv(1024).decode("utf-8", errors="ignore")
    print(" REQUISIÇÃO RECEBIDA")
    print(request)

    # primeira linha da requisição, ex: GET / HTTP/1.1
    first_line = request.split("\r\n")[0]
    parts = first_line.split()

    if len(parts) >= 2:
        method = parts[0]
        path = parts[1]
    else:
        method = ""
        path = ""

    if method == "GET" and path == "/":
        body = """
        <html>
            <head><title>Servidor Local</title></head>
            <body>
                <h1>Olá, estudante!</h1>
                <p>Seu cliente HTTP comunicou com sucesso com este servidor.</p>
            </body>
        </html>
        """
        status_line = "HTTP/1.1 200 OK\r\n"
    else:
        body = """
        <html>
            <head><title>404</title></head>
            <body>
                <h1>404 - Recurso não encontrado</h1>
            </body>
        </html>
        """
        status_line = "HTTP/1.1 404 Not Found\r\n"

    response = (
        status_line +
        "Content-Type: text/html; charset=utf-8\r\n" +
        f"Content-Length: {len(body.encode('utf-8'))}\r\n" +
        "Connection: close\r\n" +
        "\r\n" +
        body
    )

    client_socket.sendall(response.encode("utf-8"))
    client_socket.close()