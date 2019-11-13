# ninja{classics!}

from Crypto.Cipher import AES
import urllib2
    
hc = ['a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9']
flag = ''

def bf(block, suf):
    global flag
    for h1 in hc:
        for h2 in hc:
            print h1+h2
            g = h1+h2+flag+suf
            e =  urllib2.urlopen('http://ctf2.gel.webfactional.com/p1/encrypt/'+g).read()
            if (e[:32] == block):
                flag=h1+h2+flag
                #print flag
                return
    
for i in range(15, -1, -1):
    m = 'aa' + flag
    b = urllib2.urlopen('http://ctf2.gel.webfactional.com/p1/encrypt/'+m).read()[32:]
    s = chr(i).encode('hex') * i
    print i, m, s
    bf(b, s)
                
flag = flag.decode('hex')
print flag
