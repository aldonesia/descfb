import socket
import os
import sys

try:
    input = raw_input
except NameError:
    pass

def Socket():
	ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = 'localhost'
	port = 61616
	ClientSocket.connect((host, port))
	return ClientSocket

def main():
	ClientSocket = Socket()
	try:
		while True:
			choice = str(input('pilihan: \n'))
			ClientSocket.send(choice)

			key_text = str(input('key (HEX): \n'))
			ClientSocket.send(key_text)

			iv = str(input('iv (STRING): \n'))
			ClientSocket.send(iv)

			text = str(input('Text :\n'))
			ClientSocket.send(text)

			data_recv = ClientSocket.recv(4096)
			print data_recv

	except KeyboardInterrupt:
		ClientSocket.close()
		sys.exit(0)

main()


