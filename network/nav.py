import socket

s=socket.socket()

s.connect(('localhost', 8080))
s.send('GET / HTTP/1.1\n\n'.encode())

print(s.recv(512).decode())