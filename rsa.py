from Crypto.PublicKey import RSA
from Crypto.Util.number import *
import os


def key_generation(bits):
	p = getPrime(bits)
	q = getPrime(bits)
	n = p * q
	phi = (p-1) * (q-1)
	e = 3

	d = inverse(e , phi)

	return [[e,n] , [d,n]]



def encrypt(plaintext , publickey):

	e = publickey[0]
	n = publickey[1]

	return pow(plaintext ,e ,n)

def decrypt(ciphertext , privateKey):
	d = privateKey[0]
	n = privateKey[1]

	return pow(ciphertext , d, n)




if __name__ == "__main__":

	publicKey , privateKey = key_generation(1024)

	long_message = 213546546564556
	#long_message = bytes_to_long(message)

	ciphertext = encrypt(long_message , publicKey)

	print("ciphertext of" + str(long_message) + " is :" + str(ciphertext))

	plaintext = decrypt(ciphertext , privateKey)

	print((plaintext))





"""

key = RSA.generate(2048)

msg = str(input())

msg = bytes_to_long(msg)

ciphertext = pow(msg , key.e , key.n)


phi = (p-1) * (q-1)
d = inverse(e,phi)
plaintext = pow(ciphertext,d,n)

print(long_to_bytes(plaintext))
"""
