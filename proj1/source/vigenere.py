import random
import urllib2

f=file('quotes.txt','r')
quotes = [l.strip() for l in f]
f.close()
quotes = [w + chr(random.randint(ord('A'),ord('Z'))) if len(w) % 2 == 1 else w for w in quotes]

res = urllib2.urlopen('https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa.txt')
words = res.read().split()

random.shuffle(quotes)
random.shuffle(words)

def shiftEnc(c, n):
    return chr(((ord(c) - ord('A') + n) % 26) + ord('a'))

def vigenere(raw):
    key = [random.randint(1,25) for i in range(random.randint(10,20))]
    secret = "".join([shiftEnc(raw[i], key[i % len(key)]) for i in range(len(raw))])
    return secret, key
