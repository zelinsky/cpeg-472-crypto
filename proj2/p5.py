# ninja{never_r0ll_your_0wn_crypto}

from itertools import cycle, izip
import hashlib

def XOR(message, key):
    return ''.join(chr(ord(c)^ord(k)) for c,k in izip(message, cycle(key)))

enc = 'f5201c64143bb5e84e8858536a37710fb137e07764c00c76d1337b1ed73217a95a654c6918bb5a72d398e9510aca084117570baab36c6e4447a8b6a1af12c3da58b3b1119ef19435c8607134271cd154a1762368cb73396719425f104687c8962c211d85230fc93707ce70f9714dab0bde8888f34cfd3a8e7832a692e33fab42'.decode('hex')
m = "Who needs AES? I can just roll my own OFB!"
flag = ''
iv = enc[0:32]
b1 = XOR(enc[32:64], m[0:32])
flag += XOR(b1, enc[32:64])
b2 = hashlib.sha256(b1).digest()
flag += XOR(b2, enc[64:96])
b3 = hashlib.sha256(b2).digest()
flag += XOR(b3, enc[96:128])

print flag