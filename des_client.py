import socket
import os
import sys

try:
    input = raw_input
except NameError:
    pass

def Socket():
	ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = socket.gethostname()
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

			xa = input('Masukkan random key untuk alice (xa): ')
			int_xa = int(xa)
			ya = (a**int_xa)%q
			print('ini ya-> ', ya)

			xb = input('masukkan random key untuk bob (xb) : ')
			int_xb = int(xb)
			yb = (a**int_xb)%q
			print('ini yb-> ', yb)

			kabA = (int(ya)**int_xb)%q
			print ('ini kab versi alice->', kabA)

			kabB = (int(ya)**int_xb)%q
			print ('ini kab versi bob->', kabB)

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


