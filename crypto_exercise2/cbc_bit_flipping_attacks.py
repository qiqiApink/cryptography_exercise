from Crypto.Cipher import AES
from detection_oracle import generate_random_bytes
import cbc
from padding_validation import unpad
from pkcs7 import padpkcs7

key = generate_random_bytes(16)
iv = generate_random_bytes(16)

def encryptParams(userdata):
    x1 = b'comment1=cooking%20MCs;userdata='
    x2 = b';comment2=%20like%20a%20pound%20of%20bacon'
    params = x1 + userdata.encode('ascii') + x2
    return cbc.cbc_encryption(padpkcs7(params, 16), key, iv)

def decryptParamsAndCheckAdmin(encryptedParams):
    paddedParams = cbc.cbc_decryption(encryptedParams, key, iv)
    params = unpad(paddedParams)
    return params.find(b';admin=true;') != -1

x = list(encryptParams('XXXXXXXXXXXXXXXX:admin<true:XXXX'))
x[32] ^= 1
x[38] ^= 1
x[43] ^= 1
print(decryptParamsAndCheckAdmin(bytes(x)))
