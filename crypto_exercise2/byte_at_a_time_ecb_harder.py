from Crypto.Cipher import AES
from detection_oracle import generate_random_bytes
from Crypto.Random.random import randint
import base64
from pkcs7 import padpkcs7

def encryption_oracle(s):
    cipher = AES.new(key, AES.MODE_ECB)
    s = padpkcs7(prefix + s + base64.b64decode(message), 16)
    return cipher.encrypt(s)

def getBlocks(s, blocksize):
    return [s[i:i+blocksize] for i in range(0, len(s), blocksize)]

def findBlockSize():
    l = len(encryption_oracle(b''))
    i = 1
    while True:
        s = bytes([0] * i)
        t = encryption_oracle(s)
        if len(t) != l:
            return len(t) - l
        i += 1

def findPrefixBlock(blocksize):
    x1 = encryption_oracle(b'')
    x2 = encryption_oracle(b'0')
    blocks1 = getBlocks(x1, blocksize)
    blocks2 = getBlocks(x2, blocksize)
    for i in range(len(blocks1)):
        if blocks1[i] != blocks2[i]:
            return i

def findPrefixSizeModBlockSize(blocksize):
    def has_equal_block(blocks):
        for i in range(len(blocks) - 1):
            if blocks[i] == blocks[i+1]:
                return True
        return False

    for i in range(blocksize):
        s = bytes([0] * (2*blocksize + i))
        t = encryption_oracle(s)
        blocks = getBlocks(t, blocksize)
        if has_equal_block(blocks):
            return blocksize - i

    raise Exception('Not using ECB')

def findPrefixSize(blocksize):
    return blocksize*findPrefixBlock(blocksize) + findPrefixSizeModBlockSize(blocksize)

def findNextByte(blocksize, prefixsize, knownBytes):
    k1 = blocksize - (prefixsize % blocksize)
    k2 = blocksize - (len(knownBytes) % blocksize) - 1
    s = bytes([0] * (k1 + k2))
    d = {}
    for i in range(256):
        t = encryption_oracle(s + knownBytes + bytes([i]))
        d[t[prefixsize+k1:prefixsize+k1+k2 + len(knownBytes) + 1]] = i
    t = encryption_oracle(s)
    u = t[prefixsize+k1:prefixsize+k1+k2 + len(knownBytes) + 1]
    if u in d:
        return d[u]
    return None

message = b'''Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
YnkK'''
key = generate_random_bytes(16)
randcount = randint(16, 32)
prefix = generate_random_bytes(randcount)
blocksize = findBlockSize()
prefixsize = findPrefixSize(blocksize)
s = b''
while True:
    b = findNextByte(blocksize, prefixsize, s)
    if b is None:
        break
    s += bytes([b])
print(s)
