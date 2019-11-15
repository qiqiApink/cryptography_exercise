def encrypt(message, key):
    cipher = ''
    for i in range(len(message)):
        res = hex(ord(message[i])^ord(key[i%3]))[2:]
        if len(res) == 2:
            cipher += str(res)
        else:
            cipher += '0' + str(res)
    return cipher

str1 = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"
print encrypt(str1, key)
