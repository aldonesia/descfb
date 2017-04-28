import socket
import sys
import select
import os
from des_utils import *
from des_tables import *

def permutate(binary, table):
	permutated = ''
	length = len(table)
	for i in range(length):
		permutated += binary[table[i] - 1]
	return permutated


def sbox(binary):
	b = ''
	for i in range(0, len(binary), 6):
		x = int(binary[i] + binary[i + 5], 2)
		y = int(binary[i + 1:i + 5], 2)
		b += int_to_binary(SBOX[i / 6][x][y])
	return b

def convert_plain_to_binary_splitted(plain):
	plain_splitted = string_to_array(plain, 8)
	plain_binary_splitted = []
	for p in plain_splitted:
		plain_binary_splitted.append(string_to_binary(p))
	forceDebugLine()
	forceDebug('plain text           ', plain)
	forceDebug('plain splitted       ', plain_splitted)
	forceDebug('plain splitted binary', plain_binary_splitted)
	return plain_binary_splitted

def encrypt(plain, key_text, iv):
	plain_binary_splitted = convert_plain_to_binary_splitted(plain)
	block = len(plain_binary_splitted)
	
	key_bin =  convert_key_to_binary(key_text)

	iv_bin =  convert_iv_to_binary(iv)

	cd0 = permutate(key_bin, PC1)
	c = [cd0[:len(PC1) / 2]]
	d = [cd0[len(PC1) / 2:]]
	debugLine()
	debug('CD0', cd0, 7)
	for i in range(16):
		c.append(left_shift(c[i], LEFT_SHIFT[i]))
		d.append(left_shift(d[i], LEFT_SHIFT[i]))
		debug('CD' + str(i + 1), c[i + 1] + d[i + 1], 7)

	debugLine()
	k = ['']
	for i in range(16):
		k.append(permutate(c[i + 1] + d[i + 1], PC2))
		debug('K' + str(i + 1), k[i + 1], 6)

	plain_binary_splitted = [iv_bin] + plain_binary_splitted
	cipher_binary_splitted = [iv_bin]
	for i in range(block):
		temp = cipher_binary_splitted[i]

		lr0 = permutate(temp, IP)
		l = [lr0[:len(IP) / 2]]
		r = [lr0[len(IP) / 2:]]
		debugLine()
		debug('L0', l[0], 8)
		debug('R0', r[0], 8)

		 # core
		er = []
		a = ['']
		b = ['']
		pb = ['']
		for j in range(16):
			er.append(permutate(r[j], EXPANSION))
			a.append(xor(er[j], k[j + 1]))
			b.append(sbox(a[j + 1]))
			pb.append(permutate(b[j + 1], PBOX))
			r.append(xor(l[j], pb[j + 1]))
			l.append(r[j])
			debugLine()
			debug('ER' + str(j), er[j], 6)
			debug('A' + str(j + 1), a[j + 1], 6)
			debug('B' + str(j + 1), b[j + 1], 4)
			debug('PB' + str(j + 1), pb[j + 1], 8)
			debug('R' + str(j + 1), r[j + 1], 8)
			debug('L' + str(j + 1), l[j + 1], 8)

		des_k = permutate(r[16] + l[16], IP_INV)
		cipher_binary_temp = xor(plain_binary_splitted[i + 1], des_k)
		cipher_binary_splitted.append(cipher_binary_temp)
	plain_binary_splitted.remove(iv_bin)
	cipher_binary_splitted.remove(iv_bin)

	cipher_binary = ''
	cipher_hex = ''
	for c in cipher_binary_splitted:
		cipher_binary += c
		cipher_hex += convert_cipher_temp_to_hex(c)
	return cipher_hex


def decrypt(cipher, key_text, iv):
	cipher = cipher.decode('hex')
	plain_binary_splitted = convert_plain_to_binary_splitted(cipher)
	block = len(plain_binary_splitted)

	key_bin =  convert_key_to_binary(key_text)

	iv_bin =  convert_iv_to_binary(iv)

	cd0 = permutate(key_bin, PC1)
	c = [cd0[:len(PC1) / 2]]
	d = [cd0[len(PC1) / 2:]]
	debugLine()
	debug('CD0', cd0, 7)
	for i in range(16):
		c.append(left_shift(c[i], LEFT_SHIFT[i]))
		d.append(left_shift(d[i], LEFT_SHIFT[i]))
		debug('CD' + str(i + 1), c[i + 1] + d[i + 1], 7)
		
	debugLine()
	k = ['']
	for i in range(16):
		k.append(permutate(c[i + 1] + d[i + 1], PC2))
		debug('K' + str(i + 1), k[i + 1], 6)

	plain_binary_splitted = [iv_bin] + plain_binary_splitted
	cipher_binary_splitted = [iv_bin]
	for i in range(block):
		temp = plain_binary_splitted[i]

		lr0 = permutate(temp, IP)
		l = [lr0[:len(IP) / 2]]
		r = [lr0[len(IP) / 2:]]
		debugLine()
		debug('L0', l[0], 8)
		debug('R0', r[0], 8)

		 # core
		er = []
		a = ['']
		b = ['']
		pb = ['']
		for j in range(16):
			er.append(permutate(r[j], EXPANSION))
			a.append(xor(er[j], k[j + 1]))
			b.append(sbox(a[j + 1]))
			pb.append(permutate(b[j + 1], PBOX))
			r.append(xor(l[j], pb[j + 1]))
			l.append(r[j])
			debugLine()
			debug('ER' + str(j), er[j], 6)
			debug('A' + str(j + 1), a[j + 1], 6)
			debug('B' + str(j + 1), b[j + 1], 4)
			debug('PB' + str(j + 1), pb[j + 1], 8)
			debug('R' + str(j + 1), r[j + 1], 8)
			debug('L' + str(j + 1), l[j + 1], 8)

		des_k = permutate(r[16] + l[16], IP_INV)
		cipher_binary_temp = xor(plain_binary_splitted[i + 1], des_k)
		cipher_binary_splitted.append(cipher_binary_temp)
	plain_binary_splitted.remove(iv_bin)
	cipher_binary_splitted.remove(iv_bin)

	cipher_binary = ''
	cipher_hex = ''
	for c in cipher_binary_splitted:
		cipher_binary += c
		cipher_hex += convert_cipher_temp_to_hex(c)
	cipher = cipher_hex.decode('hex')
	return cipher

def Socket():
	ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	host = socket.gethostname()
	port = 61616
	ServerSocket.bind((host, port))
	ServerSocket.listen(5)
	return ServerSocket

def main():
	ServerSocket = Socket()
	inputSocket = [ServerSocket]
	try:
		while True:
			read_ready, write_ready, exception = select.select(inputSocket, [], [])
			for sock in read_ready:
				if sock == ServerSocket:
					ClientSocket, ClientAddress = ServerSocket.accept()
					inputSocket.append(ClientSocket)
				else:
					pilihan = sock.recv(1024)
					print pilihan
					
					ya = sock.recv(1024)
					q=353
					a=3

					xb = input('masukkan random key untuk bob (xb)(int) : ')
					int_xb = int(xb)
					yb = (a**int_xb)%q
					print('ini yb-> ', yb)
					yb=str(yb)
					sock.send(yb)
					

					kabB = (int(ya)**int_xb)%q
					print ('ini kab versi bob->', kabB)
					kabB=str(kabB)
					sock.send(kabB)

					kab=sock.recv(1024)
					
					print kab
					hasil=kab
					tambah = 0
					if len(hasil) < 8:
						temp_hasil = len(hasil)
						while temp_hasil < 8:
							temp_hasil = temp_hasil + 1
							key = hasil + str(tambah)
					print key

					iv = sock.recv(1024)
					print iv
					text = sock.recv(1024)
					print text
					if(pilihan == "encrypt"):
						cipher = encrypt(text, key, iv)
						sock.send(cipher)
					else:
						final = decrypt(text, key, iv)
						sock.send(final)
					return ServerSocket.close()
	except KeyboardInterrupt:
		ServerSocket.close()
		sys.exit(0)


main()