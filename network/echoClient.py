import socket
import sys

class EchoClient:
	def __init__(self, msg):
		self.__msg = msg.encode()
		self.__s = socket.socket()

	def run(self, host, port):
		self . __s . connect ( (host, port) )
		self . _send ()
		self . __s . close ()

	def _send(self):
		totalsent = 0
		while totalsent < len ( self.__msg ):
			sent = self.__s. send ( self.__msg [ totalsent :])
			totalsent += sent



msg = sys.argv[1]
addr = sys.argv[2]
port = int(sys.argv[3])

EchoClient(msg).run(addr, port)