from Crypto.Util.number import *
p=getPrime(256)
q=getPrime(256)
N=p*q
e=65537
from secret import flag
ct = pow(bytes_to_long(flag), e, N)
print (ct, e, N)
