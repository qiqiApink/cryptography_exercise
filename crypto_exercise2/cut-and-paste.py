from Crypto.Cipher import AES
from detection_oracle import generate_random_bytes
from pkcs7 import padpkcs7

def encode_profile(profile):
    s = b''
    for kv in profile:
        if s != b'':
            s += b'&'
        s += kv.encode('ascii') + b'=' + profile[kv].encode('ascii')
    return s

def profile_for(email):
    profile = {
            'email': email,
            'uid': '10',
            'role': 'user'
        }
    return encode_profile(profile)

def encrypt_profile_for(email):
    cipher = AES.new(key, AES.MODE_ECB)
    encoded_profile = padpkcs7(profile_for(email), 16)
    return cipher.encrypt(encoded_profile)

def unpadpkcs7(s, k):
    i = s[-1]
    return s[0:-i]

def decrypt_profile(s):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_profile = unpadpkcs7(cipher.decrypt(s), 16)
    pairs = decrypted_profile.split(b'&')
    profile = {}
    for p in pairs:
        k = p.split(b'=')[0].decode('ascii')
        v = p.split(b'=')[1].decode('ascii')
        profile[k] = v
    return profile

# def main():
key = generate_random_bytes(16)
email1 = 'foo@bar.coadmin' + ('\x0b' * 11)
x1 = encrypt_profile_for(email1)
email2 = 'foooo@bar.com'
x2 = encrypt_profile_for(email2)
x = x2[0:32] + x1[16:32]
y = decrypt_profile(x)
print(y)

# if __name__ == '__main__':
    # main()
