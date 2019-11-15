import base64
from Crypto.Cipher import AES

def strxor(str1, str2):
    return bytes([x ^ y for (x, y) in zip(str1, str2)])

def cbc_encryption(plaintext, key, iv):
    ciphertext = b''
    cipher = AES.new(key, AES.MODE_ECB)
    for i in range(int(len(plaintext) / len(key))):
        mblock = plaintext[i * len(key): (i+1) * len(key)]
        cblock = cipher.encrypt(strxor(mblock, iv))
        ciphertext += cblock
        iv = cblock
    return ciphertext

def cbc_decryption(ciphertext, key, iv):
    plaintext = b''
    cipher = AES.new(key, AES.MODE_ECB)
    for i in range(int(len(ciphertext) / len(key))):
        cipher_block = ciphertext[i * len(key): (i+1) * len(key)]
        plaintext += strxor(cipher.decrypt(cipher_block), iv)
        iv = cipher_block
    return plaintext

def main():
    key = 'YELLOW SUBMARINE'
    iv = b'\x00' * 16
    m = base64.b64decode(open('10.txt', 'r').read())
    if cbc_encryption(cbc_decryption(m, key, iv), key, iv) == m:
        print(1)

if __name__ == '__main__':
    main()
