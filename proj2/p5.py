# ninja{never_r0ll_your_0wn_crypto}

from itertools import cycle, izip
import hashlib

def XOR(message, key):
    return ''.join(chr(ord(c)^ord(k)) for c,k in izip(message, cycle(key)))

# Encrypted flag and message given
enc_flag = 'f5201c64143bb5e84e8858536a37710fb137e07764c00c76d1337b1ed73217a95a654c6918bb5a72d398e9510aca084117570baab36c6e4447a8b6a1af12c3da58b3b1119ef19435c8607134271cd154a1762368cb73396719425f104687c8962c211d85230fc93707ce70f9714dab0bde8888f34cfd3a8e7832a692e33fab42'.decode('hex')
message = "Who needs AES? I can just roll my own OFB!"


# OFB Mode, but sha256 used instead of AES (no key). Since the first block is known, we can find the rest.
flag = ''
iv = enc_flag[0:32]
block1 = XOR(enc_flag[32:64], message[0:32])
flag += message[0:32] #XOR(block1, enc_flag[32:64])
block2 = hashlib.sha256(block1).digest()
flag += XOR(block2, enc_flag[64:96])
block3 = hashlib.sha256(block2).digest()
flag += XOR(block3, enc_flag[96:128])

print flag
