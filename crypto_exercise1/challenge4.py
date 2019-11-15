import string

def decrypt(cipher):
    error_min = 10
    key = ''
    message = ''
    for j in range(0,256):
        string = ''
        for i in range(0, len(cipher), 2):
            res = hex(int(cipher[i:i+2],16)^j)[2:]
            if len(res) == 2:
                string += str(res)
            else:
                string += '0' + str(res)
        try:
            list1 = list(string.decode('hex').lower())
            error = 0
            for c in freqs.keys():
                error += abs(round(list1.count(c)*2.0/len(cipher),7) - freqs[c])
            if error < error_min:
                error_min = error
                key = chr(j)
                message = string.decode('hex')
        except:
            pass
    return key, message

freqs = {
        'a': 0.0651738,
        'b': 0.0124248,
        'c': 0.0217339,
        'd': 0.0349835,
        'e': 0.1041442,
        'f': 0.0197881,
        'g': 0.0158610,
        'h': 0.0492888,
        'i': 0.0558094,
        'j': 0.0009033,
        'k': 0.0050529,
        'l': 0.0331490,
        'm': 0.0202124,
        'n': 0.0564513,
        'o': 0.0596302,
        'p': 0.0137645,
        'q': 0.0008606,
        'r': 0.0497563,
        's': 0.0515760,
        't': 0.0729357,
        'u': 0.0225134,
        'v': 0.0082903,
        'w': 0.0171272,
        'x': 0.0013692,
        'y': 0.0145984,
        'z': 0.0007836,
        ' ': 0.1918182
    }

f = open('4.txt')
while True:
    cipher = f.readline()[:-1]
    if cipher:
        key, message = decrypt(cipher)
        if all(c in string.printable for c in message):
            print 'cipher = ', cipher
            print 'key = ', key
            print 'message = ', message
    else:
        break
f.close()
