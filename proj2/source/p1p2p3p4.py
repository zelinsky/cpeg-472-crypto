from flask import Flask
from Crypto.Cipher import AES

#THIS SERVER IS HOSTED AT http://ctf2.gel.webfactional.com

from secret import key1, flag1, key2, flag2, key3, flag3, key4, password, flag4
assert(len(flag1) == 16)
assert(len(flag2) == 32)

app = Flask(__name__)

def padme(msg):
    block_size = 16
    num_bytes = 16 - (len(msg) % 16)
    return msg + (num_bytes % 16)*chr(num_bytes)

def unpad(msg):
    num_bytes = ord(msg[-1])
    if msg[-num_bytes:] != msg[-1]*num_bytes:
        raise Exception("Bad Padding")
    return msg[:-num_bytes]

@app.route('/')
def index():
    return 'Usage: /p1/encrypt[/:hex] or /p2/encrypt[/:hex]'

@app.route('/p1/encrypt', defaults={"hexdigest":''})
@app.route('/p1/encrypt/', defaults={"hexdigest":''})
@app.route('/p1/encrypt/<hexdigest>')
def encrypt1(hexdigest):
    cipher = AES.new(key1,AES.MODE_ECB)
    return cipher.encrypt( padme(hexdigest.decode('hex') + flag1) ).encode('hex')

@app.route('/p2/encrypt', defaults={"hexdigest":''})
@app.route('/p2/encrypt/', defaults={"hexdigest":''})
@app.route('/p2/encrypt/<hexdigest>')
def encrypt2(hexdigest):
    cipher = AES.new(key2,AES.MODE_ECB)
    return cipher.encrypt( padme(hexdigest.decode('hex') + flag2) ).encode('hex')

@app.route('/p3/encrypt')
def encryptflag3():
    randomiv = os.urandom(16)
    cipher = AES.new(key3, AES.MODE_OFB, randomiv)
    return randomiv.encode('hex') + cipher.encrypt(flag3).encode('hex')

@app.route('/p3/encrypt/<hexdigest>/<iv>')
def encrypt3(hexdigest, iv):
    cipher = AES.new(key3, AES.MODE_OFB, padme(iv.decode('hex')))
    return cipher.encrypt(hexdigest.decode('hex')).encode('hex')

@app.route('/p4/encrypt')
def encryptpwd4():
    randomiv = os.urandom(16)
    ctr = Counter.new(128, initial_value = int(randomiv.encode('hex'), 16))
    cipher = AES.new(key4, AES.MODE_CTR, counter=ctr)
    return randomiv.encode('hex') + cipher.encrypt(padme(password)).encode('hex')

@app.route('/p4/decrypt/<hexdigest>/<iv>')
def decryptpwd4(hexdigest, iv):
    ctr = Counter.new(128, initial_value=int(iv, 16)) #IV IS HEX
    cipher = AES.new(key4, AES.MODE_CTR, counter=ctr)
    plaintext = cipher.decrypt(hexdigest.decode('hex'))
    if unpad(plaintext) == password:
        return "Do you know the password?"
    else:
        return "Ha, you don't know the password"

@app.route('/p4/flag/<yourpassword>')
def unlockflag4(yourpassword):
    if yourpassword == password:
        return flag4
