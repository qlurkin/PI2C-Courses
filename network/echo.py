import socket
import sys

class EchoServer:
	def __init__(self, host, port):
		self.__s = socket.socket()
		self.__s.bind((host, port))
		
	def run(self):
		self . __s . listen ()
		while True :
			client , addr = self . __s . accept ()
			print ( self . _receive ( client ) )
			client . close ()

	def _receive(self, client):
		chunks = []
		finished = False
		while not finished :
			data = client . recv (1024)
			chunks . append ( data )
			finished = data == b''
		return b''. join ( chunks ) . decode ()
	

host = sys.argv[1]
port = int(sys.argv[2])

EchoServer(host, port).run()