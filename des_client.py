import socket
import os
import sys

try:
    input = raw_input
except NameError:
    pass

def Socket():
	ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#<<<<<<< HEAD
	#host = '10.151.43.167'
#=======
	host = socket.gethostname()
#>>>>>>> ffac0712b5f1d9a5a0b19a5b2d322b966fae48d6
	port = 61616
	ClientSocket.connect((host, port))
	return ClientSocket

def main():
	ClientSocket = Socket()
	try:
		while True:
			choice = str(input('pilihan: \n'))
			ClientSocket.send(choice)

			#key_text = str(input('key (HEX): \n'))
			#ClientSocket.send(key_text)

			q=353
			a=3

			xa = input('Masukkan random key untuk alice (xa) (int) : ')
			int_xa = int(xa)
			ya = (a**int_xa)%q
			print('ini ya-> ', ya)
			ya = str(ya)
			ClientSocket.send(ya)
			yb = ClientSocket.recv(1024)

			kabA = (int(yb)**int_xa)%q
			print ('ini kab versi alice->', kabA)

			kabB = ClientSocket.recv(1024)
			kabB = int(kabB)
			if (kabA == kabB):
				kab=str(kabA)
				ClientSocket.send(kab)
			else:
				return ClientSocket.close()

			iv = str(input('iv (STRING): \n'))
			ClientSocket.send(iv)

			text = str(input('Text :\n'))
			ClientSocket.send(text)

			data_recv = ClientSocket.recv(4096)
			print 'hasil : '+data_recv
			return ClientSocket.close()
	except KeyboardInterrupt:
		ClientSocket.close()
		sys.exit(0)

main()


