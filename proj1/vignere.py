'''
Matthew Zelinsky
Viginere
Key Length = 17
Key = uytjktlpcrkxznryh

howqu ickco methe reaso nsfor appro vingw hatwe likei havea lways thoug httha tawil danim alnev erloo kssow ellas whens omeob stacl eofpr onoun ceddu rabil ityis betwe enusa perso nalex perie nceha sinte nsifi edrat herth andim inish edtha tidea wheny ouvel earne dtola ughat theth ingst hatsh ouldb elaug hedat andno ttola ughat those thats hould ntyou vegot wisdo mandu nders tandi ngtre acher yandv iolen ceare spear spoin tedat bothe ndsth eywou ndtho sewho resor ttoth emwor setha nthei renem iesth ereis nosuc hthin gasun mixed evila manwh olose shism oneyg ainsa tleas texpe rienc eands ometi messo methi ngbet terhe thatw antsm oneym eansa ndcon tenti swith outth reego odfri endsl aught erisp oison tofea r
'''

normal_freqs = {'a': 0.080642499002080981, 'c': 0.026892340312538593, 'b': 0.015373768624831691, 'e': 0.12886234260657689, 'd': 0.043286671390026357, 'g': 0.019625534749730816, 'f': 0.024484713711692099, 'i': 0.06905550211598431, 'h': 0.060987267963718068, 'k': 0.0062521823678781188, 'j': 0.0011176940633901926, 'm': 0.025009719347800208, 'l': 0.041016761327711163, 'o': 0.073783151266212627, 'n': 0.069849754102356679, 'q': 0.0010648594165322703, 'p': 0.017031440203182008, 's': 0.063817324270355996, 'r': 0.06156572691936394, 'u': 0.027856851020401599, 't': 0.090246649949305979, 'w': 0.021192261444145363, 'v': 0.010257964235274787, 'y': 0.01806326249861108, 'x': 0.0016941732664605912, 'z': 0.0009695838238376564}

cipher = 'bmpzebnzefwbsuvpluqhwcyzgcgzonizlnqftcgxwxmvsezivysqyrbdazjiydqgnkydcjwjxbxpneosdecmveqlxgxwacjgedajmtymubdtnagfpmqbembhaxmnncpdzvfslzqiyrpnogfhcgoorbeysyvinbbpcevrxrverlhqbosxogckrbqgyyuxgfrxbdwgudezgzbluuanxrzjxvvbzeecknmejezspvkrbsuzlnmrajdlsdwcnydyrsnbcwjdtyspfdqnyrsnbymcrhdtvykqrufssxlmhyngtifdthfumtulwdxwpgukkkcveealctlrxcncenshbccuwctaolatcicmnverlxymkymstpucqgrpuvolwcrhdtyyyodffpanmmqofhdtjoqgneroygknxxxxgjdedevgzhmldmaewkeqxrhekprcwnfbwporxtgbcmzyqarcfzcgpqxhajyafctbdxiegisbmpvyuxqhvomtbgjcllrkfpheundmpgjvdezgnyunqfxxxjbgrxpzauavhrxwdbdlkkrltgkfyyczxywqgkvxaryrsnbrxasladkjyksbwchl'



# Shift char c by n
def shiftBy(c, n):
    return chr(((ord(c) - ord('a') + n) % 26) + ord('a'))


freqs = [] # Fr
keyLength = 17

for i in range(keyLength):
    frequency = {}
    tenth = cipher[i::keyLength]
    for ascii in range(ord('a'), ord('a')+26):
        frequency[chr(ascii)] = float(tenth.count(chr(ascii)))/len(tenth)
    freqs.append(frequency)

for idx, f in enumerate(freqs):
    sqr = 0.0
    for l in f:
        sqr += f[l]*f[l]
    print str(idx) + ": " + str(sqr)
    
key = ""    

for idx, f in enumerate(freqs):
    for poss_key in range(1, 26):
        sum_f_sqr = 0.0
        for l in normal_freqs:
            guess = shiftBy(l, poss_key)
            sum_f_sqr += normal_freqs[l]*f[guess]
        if abs(sum_f_sqr - 0.065) < 0.01:
            print "Possible ", idx, " key is ", chr(poss_key + ord('a')), ": ", sum_f_sqr
            key += chr(poss_key + ord('a'))

key = 'uytjktlpcrkxznryh'

# Unshift c by n
def shiftBy_d(c, n):
    return chr(((ord(c) - ord('a') - (ord(n) - ord('a'))) % 26) + ord('a'))

# Decode
def decode(raw, key):
    secret = "".join([shiftBy_d(raw[i], key[i % len(key)]) for i in range(len(raw))])
    withSpaces = ''
    for i in range(len(secret)):
        if i % 5 == 4:
            withSpaces = withSpaces + secret[i] + ' '
        else:
            withSpaces = withSpaces + secret[i]
    return withSpaces

plain = decode(cipher, key)

print "Key: ", key
print plain
