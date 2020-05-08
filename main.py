from tkinter import Tk
from tkinter.filedialog import askopenfilename
import Crypto
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from gui import *
#################################################

salt = b')Ik\xb7\x17\xb7)\x97o\t\xfaB\x0c\xbb\xab\xe2\xa1\x08\xcb\xebS\x12\xe5\xe6\x7fC\xc4P/\x14\xad\xa2'
password = get_password()
key = PBKDF2(password, salt, dkLen=32) # 256 bits for aes256
print(key)
