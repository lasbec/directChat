from threading import Thread
import os

class Chat:
	def __init__(self, sock):
		self.receiver = ReceiverThread(sock)
		self.sender = SenderThread(sock)

	def start(self):
		os.system('clear')
		print('connected')
		self.receiver.start()
		self.sender.start()

class ReceiverThread(Thread):
	def __init__(self, sock):
		Thread.__init__(self)
		self.sock = sock
	
	def run(self):
		while True:
			msg = self.sock.recv(4098)
			print('partner: ' + msg.decode())

class SenderThread(Thread):
	def __init__(self, sock):
		Thread.__init__(self)
		self.sock = sock

	def run(self):
		while True:
			msg = input()
			self.sock.send(msg.encode())
