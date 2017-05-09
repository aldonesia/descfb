import random
import math

def generaten(p,q):
	n = p*q
	return n

def generatem(p,q):
	m = (p-1)*(q-1)
	return m

def gcd(a, b):
	for n in range(2, min(a, b) + 1):
		if a % n == b % n == 0:
			return False
	return True

def publickey(m):
	for i in range(3, m, 2):
		i = random.randint(3,m)
		if gcd(i, m) == 1:
			e = i
			break
	return e

def privatekey(m, public_key):
	for i in range(3, m, 2):
		if i * public_key % m == 1:
			d = i
			break
	return d

def encryptrsa(text, public_key, n):
	cipher = [(ord(char) ** public_key) % n for char in text]
	final_encrypt = ''.join(map(str,cipher))
	print final_encrypt
	return cipher

def decryptrsa(text, private_key, n):
	plain = [chr((char ** private_key) % n) for char in text]
	return ''.join(plain)
