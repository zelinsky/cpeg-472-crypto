import random
import gmpy2
from Crypto.Util.number import *

p=getPrime(1024)
q=int(gmpy2.next_prime(p + random.randint(2, 2**128)))
N=p*q
e=65537

from secret import flag
ct = pow(bytes_to_long(flag), e, N)
print (ct, e, N)
