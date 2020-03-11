import socket

with open('resp.txt') as file:
	response = file.read()

s = socket.socket()

s.bind(('0.0.0.0', 8080))

s.listen()

client, address = s.accept()

print(client.recv(512).decode())
client.send(response.encode())