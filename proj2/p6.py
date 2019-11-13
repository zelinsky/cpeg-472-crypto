# ninja{b1t_fl1pp1ng_1n_CBC_dang?}

from Crypto.Cipher import AES
import urllib2
from itertools import cycle, izip

def XOR(message, key):
    return ''.join(chr(ord(c)^ord(k)) for c,k in izip(message, cycle(key)))
    
r =  urllib2.urlopen('http://ctf1.gel.webfactional.com/p6/cookie').read()
iv = r[:32]
enc_c = r[32:]

c = '{nm:guest,flg:0}'
d = XOR(c, iv.decode('hex'))

new_iv = iv[0:8]+XOR(d[4:9], 'admin').encode('hex')+iv[18:28]+XOR(d[14:15], '1').encode('hex')+iv[30:]

r =  urllib2.urlopen('http://ctf1.gel.webfactional.com/p6/login/'+enc_c+'/'+new_iv).read()
print r

