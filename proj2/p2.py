# ninja{is_it_d1ff3r3nt?_withmore}

from Crypto.Cipher import AES
import urllib2
import string
import itertools


hexdigits = string.hexdigits[:-6]
flag1 = ''
flag2 = ''


def brute_force_byte(block, padding, f):

    # Loop through hex values
    for h in map(''.join, itertools.product(hexdigits, repeat=2)):
        print h
        g = h+f+padding
        e =  urllib2.urlopen('http://ctf2.gel.webfactional.com/p2/encrypt/'+g).read()
        if (e[:32] == block):
            f=h+f
            return f

# Loop through the last 16 bytes of the flag
for i in range(15, -1, -1):
    m = 'aa' + flag1

    # First byte of block3 is the byte we have to brute force, the rest of the block is padding
    block3 = urllib2.urlopen('http://ctf2.gel.webfactional.com/p2/encrypt/'+m).read()[64:96]
    padding = chr(i).encode('hex') * i
    print i, m, padding
    flag1 = brute_force_byte(block3, padding, flag1)

# Loop through the first 16 bytes of the flag
# Padding here is actually part of flag1
for i in range(15, -1, -1):
    m = 'aa' + flag2

    # First byte of block2 has to be brute forced, the rest of the block is part of flag1 we found previously
    block3 = urllib2.urlopen('http://ctf2.gel.webfactional.com/p2/encrypt/'+m).read()[32:64]
    padding = flag1[:i*2]
    print i, m, padding
    flag2 = brute_force_byte(block3, padding, flag2)
                
flag = (flag2+flag1).decode('hex')
print flag
