import socket
import os
import sys
import pickle
import cPickle
from rsa import *

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
			p = input('masukkan bilangan prima : ')
			ClientSocket.send(str(p))
			q = input('masukkan bilangan prima yang berbeda dengan pertama : ')
			ClientSocket.send(str(q))

			n=ClientSocket.recv(1024)
			n=int(n)
			print('n = ', n)

			public_key = ClientSocket.recv(1024)
			public_key = int(public_key)
			print('Public Key = ', public_key)
			done='terkirim'
			ClientSocket.send(done)
			private_key = ClientSocket.recv(1024)
			private_key = int(private_key)
			print('Private Key = ', private_key)

			pesan1 = ClientSocket.recv(1024)
			q_encrypt = pickle.load(open("encrypt_q","rb"))
			q = decryptrsa(q_encrypt, private_key, n)
			print('q = ', q)
			q= int(q)

			pesan2 = ClientSocket.recv(1024)
			a_encrypt = pickle.load(open("encrypt_a","rb"))
			a = decryptrsa(a_encrypt, private_key, n)
			print('a = ', a)
			a = int(a)

			choice = str(input('pilihan: \n'))
			ClientSocket.send(choice)

			#key_text = str(input('key (HEX): \n'))
			#ClientSocket.send(key_text)

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


