# ninja{classics!}

from Crypto.Cipher import AES
import urllib2
import itertools
import string
    
flag = ''

hexdigits = string.hexdigits[:-6]


def brute_force_byte(block, padding):
    global flag

    # Loop through hex values
    for h in map(''.join, itertools.product(hexdigits, repeat=2)):
        print h
        guess = h+flag+padding
        encryption = urllib2.urlopen('http://ctf2.gel.webfactional.com/p1/encrypt/'+guess).read()

        # If the encryption of our guess is equal to the encrypted block we have, our guess if correct, prepend to existing flag
        if (encryption[:32] == block):
            flag=h+flag
            return

# Loop through bytes in the flag: 15...0
# i is i'th byte of flag
for i in range(15, -1, -1):
    message = 'aa' + flag # Message to be encrypted

    # First byte of block2 is the i'th byte of the flag that we have to brute force
    block2 = urllib2.urlopen('http://ctf2.gel.webfactional.com/p1/encrypt/'+message).read()[32:]

    # We know the padding of the 2nd block is
    padding = chr(i).encode('hex') * i
    print i, message, padding
    brute_force_byte(block2, padding)
                
flag = flag.decode('hex')
print flag
