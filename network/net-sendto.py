import socket

s = socket.socket(type=socket.SOCK_DGRAM)

data = "Yop".encode()
sent = s.sendto(data, ('localhost', 5000))
print(sent)
if sent == len(data):
	print("OK")