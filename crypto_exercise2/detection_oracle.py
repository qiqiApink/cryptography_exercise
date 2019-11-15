from pkcs7 import padpkcs7
from cbc import cbc_encryption
from Crypto.Cipher import AES
from Crypto.Random.random import randint

def generate_random_bytes(num_bytes):
    return bytes([randint(0, 255) for i in range(num_bytes)])

def encryption_oracle(s):
    key = generate_random_bytes(16)
    s = generate_random_bytes(randint(5, 10)) + s + generate_random_bytes(randint(5, 10))
    s = padpkcs7(s, 16)
    if randint(0, 1) == 0:
        print('Encrypting with ECB')
        cipher = AES.new(key, AES.MODE_ECB)
        return cipher.encrypt(s)
    else:
        print('Encrypting with CBC')
        iv = generate_random_bytes(16)
        return cbc_encryption(s, key, iv)

def detection():
    s = bytes([0] * 43)
    t = encryption_oracle(s)
    if t[16:32] == t[32:48]:
        return 'detection: ECB'
    return 'detection: CBC'

if __name__ == '__main__':
    print(detection())
