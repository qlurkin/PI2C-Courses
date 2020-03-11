import socket

s = socket.socket(type=socket.SOCK_DGRAM)

s.bind(('0.0.0.0', 5000))

data = s.recvfrom(512)
print("Reçu: {}, from: {}".format(data[0].decode(), data[1]))