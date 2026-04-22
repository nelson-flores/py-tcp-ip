import socket

HOST = "127.0.0.1"
PORT = 8080
PATH = "/"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

request = (
    f"GET {PATH} HTTP/1.1\r\n"
    f"Host: {HOST}:{PORT}\r\n"
    "Connection: close\r\n"
    "\r\n"
)

client.sendall(request.encode("utf-8"))

response = b""
while True:
    data = client.recv(1024)
    if not data:
        break
    response += data

client.close()

print(response.decode("utf-8", errors="ignore"))