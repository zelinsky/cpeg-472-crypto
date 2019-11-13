# ninja{kn0ck_knock_NE0_follow_the_wh1te_rabbit}

from Crypto.Cipher import AES
import urllib2
from itertools import cycle, izip

def XOR(message, key):
    return ''.join(chr(ord(c)^ord(k)) for c,k in izip(message, cycle(key)))
    
hc = ['a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9']

r = urllib2.urlopen('http://ctf2.gel.webfactional.com/p4/encrypt').read()

iv = r[0:32]
enc = r[32:].decode('hex')

for i in range(0, len(enc)):
    my_enc = enc[:i] + XOR('a', enc[i]) + enc[i+1:]
    try:
        urllib2.urlopen('http://ctf2.gel.webfactional.com/p4/decrypt/'+my_enc.encode('hex')+'/'+iv).read()
    except:
        pad = len(enc) - i
        break
    
f = chr(pad) * pad
k = XOR(enc[-pad:], f)

def bf(n):
    global k
    for h1 in hc:
        for h2 in hc:
            my_enc = enc[:16-n]+(h1+h2).decode('hex')+XOR(chr(n)*(n-1), k)
            try:
                urllib2.urlopen('http://ctf2.gel.webfactional.com/p4/decrypt/'+my_enc.encode('hex')+'/'+iv).read()
                k = XOR((h1+h2).decode('hex'), chr(i))+k
                return
            except:
                pass
            
for i in range(pad+1, 17):
    bf(i)

password = XOR(enc, k)[:-pad]
flag = urllib2.urlopen('http://ctf2.gel.webfactional.com/p4/flag/'+password).read()
print flag