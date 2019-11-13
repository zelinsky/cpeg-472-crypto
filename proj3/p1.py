# ninja{w3ll_it_is_h4rd_t0_k33p_s3cure_w_an_oracle}

import urllib2
from Crypto.Util.number import *

n, e, ct = urllib2.urlopen('http://ctf3.gel.webfactional.com/p1/encrypt/').read().replace('(', '').replace(')', '').replace('L', '').split(',')
ct = int(ct)
e = int(e)
n = int(n)
ct_2 = ct*pow(2, e) % n
pt_2 = urllib2.urlopen('http://ctf3.gel.webfactional.com/p1/decrypt/' + (hex(ct_2))[2:-1]).read()
pt_2 = int(pt_2)
pt = pt_2/2
flag = long_to_bytes(pt)
print flag
