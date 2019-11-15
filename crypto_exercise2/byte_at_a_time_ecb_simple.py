from Crypto.Cipher import AES
import base64
from pkcs7 import padpkcs7
from detection_oracle import generate_random_bytes

# key = generate_random_bytes(16)
def encryption_oracle(s):
    cipher = AES.new(key, AES.MODE_ECB)
    s = padpkcs7(s + base64.b64decode(message), 16)
    return cipher.encrypt(s)

def findBlockSize():
    l = len(encryption_oracle(b''))
    i = 1
    while True:
        s = bytes([0] * i)
        t = encryption_oracle(s)
        if len(t) != l:
            return len(t) - l
        i += 1

def confirmECB(blocksize):
    s = generate_random_bytes(blocksize) * 2
    t = encryption_oracle(s)
    if t[0:blocksize] != t[blocksize:2*blocksize]:
        raise Exception('Not using ECB')

def findNextByte(blocksize, knownBytes):
    s = bytes([0] * (blocksize - (len(knownBytes) % blocksize) - 1))
    d = {}
    for i in range(256):
        t = encryption_oracle(s + knownBytes + bytes([i]))
        d[t[0:len(s) + len(knownBytes) + 1]] = i
    t = encryption_oracle(s)
    u = t[0:len(s) + len(knownBytes) + 1]
    if u in d:
        return d[u]
    return None

# def main():
message = b'''Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
YnkK'''
blocksize = findBlockSize()
confirmECB(blocksize)
s = b''
while True:
    b = findNextByte(blocksize, s)
    if b is None:
        break
    s += bytes([b])
print(s)

# if __name__ == '__main__':
    # main()
