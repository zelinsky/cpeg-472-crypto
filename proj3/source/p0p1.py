from flask import Flask
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Util.number import *
#has long_to_bytes, bytes_to_long, GCD
import os
import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'Usage: /p0/encrypt[/:hex]'

from secret import flag0

@app.route('/p0/encrypt')
@app.route('/p0/encrypt/')
def encryptFlag0():
    p=getPrime(1024)
    q=getPrime(1024)
    N = p*q
    e = 17
    return str( (N,e,pow(bytes_to_long(flag0), e, N)) )

from secret import flag1, N1, e1, d1, ct1

@app.route('/p1/encrypt')
@app.route('/p1/encrypt/')
def encryptFlag1():
    return str( (N1, e1, pow(bytes_to_long(flag1), e1, N1)) )

@app.route('/p1/decrypt/<hexdigest>')
def decryptFlag1(hexdigest):
    desired = int(hexdigest, 16)
    if desired == ct1:
        return "0"
    return str( pow(desired, d1, N1) )
