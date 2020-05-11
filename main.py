from tkinter import Tk
from tkinter.filedialog import askopenfilename
import Crypto
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from gui import *
#################################################
salt = b')Ik\xb7\x17\xb7)\x97o\t\xfaB\x0c\xbb\xab\xe2\xa1\x08\xcb\xebS\x12\xe5\xe6\x7fC\xc4P/\x14\xad\xa2'
password = get_password()
key = PBKDF2(password, salt, dkLen=32) # 256 bits for aes256 using Password-Based Key Derivation Function
buffer_size = 10000
data = 'the world is a vampire'
test_file = 'test.jpg'
cipher = AES.new(key, AES.MODE_CFB) # CFB mode
'''
in_file = open(test_file,'rb')
out_file = open(test_file+'.hax','wb')
out_file.write(cipher.iv)
buffer = in_file.read(buffer_size)
while len(buffer) > 0:
    ciphered_bytes = cipher.encrypt(buffer)
    out_file.write(ciphered_bytes)
    buffer = in_file.read(buffer_size)
'''
def encrypt(file_name):
	fin = open(file_name,'rb')
	fout = open(file_name + '.pylocker','wb')
	buffer  = fin.read(buffer_size)
	fout.write(cipher.iv)
	while(len(buffer)>0):
		ciph = cipher.encrypt(buffer)
		fout.write(ciph)
		buffer = fin.read(buffer_size)
		
encrypt(test_file)
