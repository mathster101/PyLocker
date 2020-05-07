from Crypto.Random import get_random_bytes
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import Crypto


Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

filename = askopenfilename() 

t = open(filename,'rb')
k = t.readlines()

print(k)
