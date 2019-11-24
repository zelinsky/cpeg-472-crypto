# ninja{b1t_fl1pp1ng_1n_CBC_dang?}

from Crypto.Cipher import AES
import urllib2
from itertools import cycle, izip

def XOR(message, key):
    return ''.join(chr(ord(c)^ord(k)) for c,k in izip(message, cycle(key)))

# Get the iv and encrypted cookie (AES CBC mode)
response =  urllib2.urlopen('http://ctf1.gel.webfactional.com/p6/cookie').read()
iv = response[:32]
enc_cookie = response[32:]

# Unencrypted cookie
cookie = '{nm:guest,flg:0}'

# Output of decrypted cookie before being xor'd with IV
d = XOR(cookie, iv.decode('hex'))

# Generate a new iv with flipped values
new_iv = iv[0:8]+XOR(d[4:9], 'admin').encode('hex')+iv[18:28]+XOR(d[14:15], '1').encode('hex')+iv[30:]

flag =  urllib2.urlopen('http://ctf1.gel.webfactional.com/p6/login/'+enc_cookie+'/'+new_iv).read()
print flag

