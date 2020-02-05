from socket import *
from sys import argv
from chat import Chat

my_ip = 'localhost' if len(argv) == 0 else ''
my_port = 8080

listener = socket()
listener.bind((my_ip, my_port))
listener.listen(3)

print('listening on ipaddress: ' + str(gethostbyname(gethostname())) )

valid_conn = False
while not valid_conn:
	sock, addr = listener.accept()
	#validate connection
	valid_conn = True

Chat(sock).start()
