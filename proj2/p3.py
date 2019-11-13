# ninja{not_s0_diff3rent_th4n_OTP}

from Crypto.Cipher import AES
import urllib2
from itertools import cycle, izip

def XOR(message, key):
    return ''.join(chr(ord(c)^ord(k)) for c,k in izip(message, cycle(key)))

r = urllib2.urlopen('http://ctf2.gel.webfactional.com/p3/encrypt').read()
iv = r[:32]
enc_flag = r[32:].decode('hex')

my_pt = 'a' * 32
my_enc = urllib2.urlopen('http://ctf2.gel.webfactional.com/p3/encrypt/'+my_pt.encode('hex')+'/'+iv).read().decode('hex')

b1 = XOR(my_pt[:16], my_enc[:16])
b2 = XOR(my_pt[16:], my_enc[16:])

flag = XOR(b1, enc_flag[:16]) + XOR(b2, enc_flag[16:])
print flag