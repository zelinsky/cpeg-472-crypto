# ninja{kn0ck_knock_NE0_follow_the_wh1te_rabbit}

from Crypto.Cipher import AES
import urllib2
from itertools import cycle, izip, product
import string

def XOR(message, key):
    return ''.join(chr(ord(c)^ord(k)) for c,k in izip(message, cycle(key)))
    
hexdigits = string.hexdigits[:-6]

# Get the AES CTR encrypted password and IV
response = urllib2.urlopen('http://ctf2.gel.webfactional.com/p4/encrypt').read()
iv = response[0:32]
enc_pass = response[32:].decode('hex') # 16 bytes


# Find the (length of) the padding for the password
# Iterate through encrypted password byte by byte, changing the byte, and then trying to decrypt
# If a padding error is received, we know we changed the first byte of the padding
for i in range(0, len(enc_pass)):
    my_enc = enc_pass[:i] + XOR('a', enc_pass[i]) + enc_pass[i+1:]
    try:
        urllib2.urlopen('http://ctf2.gel.webfactional.com/p4/decrypt/'+my_enc.encode('hex')+'/'+iv).read()
    except:
        pad = len(enc_pass) - i
        break

# Xor the padding in the encrypted password with the plaintext padding to get the output of the AES CTR, we'll call this k
padding = chr(pad) * pad
k = XOR(enc_pass[-pad:], padding)

# Brute force the n'th byte (starting from the end) of the encrypted password
def brute_force(n):
    global k
    # Loop through possible byte values
    for h in map(''.join, product(hexdigits, repeat=2)):

        # The encrypted padding for finding the n'th byte, will decrypt to correct padding
        enc_padding = XOR(chr(n)*(n-1), k)

        # Guess what the encrypted first byte of the padding is
        my_enc = enc_pass[:16-n]+(h).decode('hex')+enc_padding

        # If it decrypts successfully, our guess was correct
        try:
            urllib2.urlopen('http://ctf2.gel.webfactional.com/p4/decrypt/'+my_enc.encode('hex')+'/'+iv).read()

            # Success, we found the next byte of k
            k = XOR((h).decode('hex'), chr(n))+k
            return
        except:
            pass

# Brute force the rest of the password
for i in range(pad+1, 17):
    brute_force(i)
password = XOR(enc_pass, k)[:-pad]

# We can get the flag now that we have the password
flag = urllib2.urlopen('http://ctf2.gel.webfactional.com/p4/flag/'+password).read()
print flag
