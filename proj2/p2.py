# ninja{is_it_d1ff3r3nt?_withmore}

from Crypto.Cipher import AES
import urllib2
    
hc = ['a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9']
flag1 = ''
flag2 = ''

def bf(block, suf, f):
    for h1 in hc:
        for h2 in hc:
            g = h1+h2+f+suf
            e =  urllib2.urlopen('http://ctf2.gel.webfactional.com/p2/encrypt/'+g).read()
            if (e[:32] == block):
                f=h1+h2+f
                #print f
                return f
 
for i in range(15, -1, -1):
    m = 'aa' + flag1
    b = urllib2.urlopen('http://ctf2.gel.webfactional.com/p2/encrypt/'+m).read()[64:96]
    s = chr(i).encode('hex') * i
    #print i, m, s
    flag1 = bf(b, s, flag1)
    
for i in range(15, -1, -1):
    m = 'aa' + flag2 + flag1
    b = urllib2.urlopen('http://ctf2.gel.webfactional.com/p2/encrypt/'+m).read()[64:96]
    s = flag1[:i*2]
    #print i, m, s
    flag2 = bf(b, s, flag2)
                
flag = (flag2+flag1).decode('hex')
print flag