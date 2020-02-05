from socket import *
from sys import argv
from chat import Chat

partner_ip = argv[1]
partner_port = 8080

sock = socket()
sock.connect((partner_ip, partner_port))

# verify connection

Chat(sock).start()