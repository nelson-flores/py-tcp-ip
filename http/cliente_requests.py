import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print(" LINHA DE STATUS")
print(f"{response.status_code} {response.reason}")

print("\n CABEÇALHOS")
for key, value in response.headers.items():
    print(f"{key}: {value}")

print("\n CORPO (texto)")
print(response.text)

print("\n CORPO (JSON convertido para Python)")
print(response.json())