# ninja{AES_modes_are_really_just_ECB_ALL_THE_WAY}

from Crypto.Cipher import AES
import urllib2
from itertools import cycle, izip

def XOR(message, key):
    return ''.join(chr(ord(c)^ord(k)) for c,k in izip(message, cycle(key)))

ct = urllib2.urlopen('http://ctf1.gel.webfactional.com/p0/getflag').read()
iv = ct[0:32]
b0 = ct[32:64]
b1 = ct[64:96]
b2 = ct[96:128]

url = 'http://ctf1.gel.webfactional.com/p0/decryptblock/'
m0 = XOR(urllib2.urlopen(url+b0).read().decode('hex'), iv.decode('hex'))
m1 = XOR(urllib2.urlopen(url+b1).read().decode('hex'), b0.decode('hex'))
m2 = XOR(urllib2.urlopen(url+b2).read().decode('hex'), b1.decode('hex'))
m = m0+m1+m2
print m
