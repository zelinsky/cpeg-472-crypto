# ninja{AES_modes_are_really_just_ECB_ALL_THE_WAY}

from Crypto.Cipher import AES
import urllib2
from itertools import cycle, izip

def XOR(message, key):
    return ''.join(chr(ord(c)^ord(k)) for c,k in izip(message, cycle(key)))


# Get the ciphertext, AES CBC mode
ct = urllib2.urlopen('http://ctf1.gel.webfactional.com/p0/getflag').read()

# Separate into iv and 16-byte blocks
iv = ct[0:32]
block0 = ct[32:64]
block1 = ct[64:96]
block2 = ct[96:128]

# Decrypt each block using ECB mode
url = 'http://ctf1.gel.webfactional.com/p0/decryptblock/'
m0 = XOR(urllib2.urlopen(url+block0).read().decode('hex'), iv.decode('hex'))
m1 = XOR(urllib2.urlopen(url+block1).read().decode('hex'), block0.decode('hex'))
m2 = XOR(urllib2.urlopen(url+block2).read().decode('hex'), block1.decode('hex'))
m = m0+m1+m2
print m
