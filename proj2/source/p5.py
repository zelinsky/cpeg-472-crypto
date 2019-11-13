import hashlib
import os
from itertools import cycle, izip
from secret import flag

def XOR(message, key):
        return ''.join(chr(ord(c)^ord(k)) for c,k in izip(message, cycle(key)))

def THE_NO_AES_OFB_encryption(plaintext, secret):
    iv = os.urandom(32)
    ct=iv
    nextblock = iv + secret
    for i in range(0, len(plaintext), 32):
        nextblock = hashlib.sha256(nextblock).digest()
        ct += XOR(nextblock, plaintext[i:i+32])
    return ct

password = os.urandom(32)
plaintext="Who needs AES? I can just roll my own OFB!"+flag
ct = THE_NO_AES_OFB_encryption(plaintext, password)

f=file('ciphertext.txt','w')
f.write(ct.encode('hex'))
f.close()

#YORO == "You Only Roll Once"import hashlib
import os
from itertools import cycle, izip
from secret import flag

def XOR(message, key):
        return ''.join(chr(ord(c)^ord(k)) for c,k in izip(message, cycle(key)))

def THE_NO_AES_OFB_encryption(plaintext, secret):
    iv = os.urandom(32)
    ct=iv
    nextblock = iv + secret
    for i in range(0, len(plaintext), 32):
        nextblock = hashlib.sha256(nextblock).digest()
        ct += XOR(nextblock, plaintext[i:i+32])
    return ct

password = os.urandom(32)
plaintext="Who needs AES? I can just roll my own OFB!"+flag
ct = THE_NO_AES_OFB_encryption(plaintext, password)

f=file('ciphertext.txt','w')
f.write(ct.encode('hex'))
f.close()

#YORO == "You Only Roll Once"
