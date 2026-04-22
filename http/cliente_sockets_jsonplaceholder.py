import socket

HOST = "jsonplaceholder.typicode.com"
PORT = 80
PATH = "/posts/1"

# cria socket TCP/IP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# conecta ao servidor
client.connect((HOST, PORT))

# monta a requisição HTTP manualmente
request = (
    f"GET {PATH} HTTP/1.1\r\n"
    f"Host: {HOST}\r\n"
    "Connection: close\r\n"
    "\r\n"
)

# envia a requisição
client.sendall(request.encode("utf-8"))

# recebe a resposta completa
response = b""
while True:
    data = client.recv(1024)
    if not data:
        break
    response += data

# fecha a conexão
client.close()

# converte bytes para texto
response_text = response.decode("utf-8", errors="ignore")

print(" RESPOSTA COMPLETA")
print(response_text)

# separa cabeçalhos e corpo
parts = response_text.split("\r\n\r\n", 1)

if len(parts) == 2:
    headers, body = parts
else:
    headers = response_text
    body = ""

print("\n CABEÇALHOS")
print(headers)

print("\n CORPO (JSON)")
print(body)