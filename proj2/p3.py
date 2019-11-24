# ninja{not_s0_diff3rent_th4n_OTP}

from Crypto.Cipher import AES
import urllib2
from itertools import cycle, izip

def XOR(message, key):
    return ''.join(chr(ord(c)^ord(k)) for c,k in izip(message, cycle(key)))

# Get the AES OFB encrypted flag and IV
response = urllib2.urlopen('http://ctf2.gel.webfactional.com/p3/encrypt').read()
iv = response[:32]
enc_flag = response[32:].decode('hex') # 32 bytes

# Encrypt something I know the plain text of; encrypted with same key and IV
my_pt = 'a' * 32
my_enc = urllib2.urlopen('http://ctf2.gel.webfactional.com/p3/encrypt/'+my_pt.encode('hex')+'/'+iv).read().decode('hex')

# XOR of my plaintext and my ciphertext are the same blocks the flag was xor'd with
ofb_block = XOR(my_pt, my_enc)

flag = XOR(ofb_block, enc_flag)
print flag
