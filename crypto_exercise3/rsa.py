def EGCD(e, et):
    if et == 0:
        return 1, 0, e
    else:
        x, y, q = EGCD(et, e % et)
        # q = gcd(a, b) = gcd(b, a%b)
        x, y = y, (x - (e // et) * y)
        return x, y, q

def invmod(e, et):
    x, y, q = EGCD(e, et)
    return x % et

def encrypt(m, e, n):
    return m**e % n

def decrypt(c, d, n):
    return c**d % n

p = 47
q = 17
n = p * q
phi_n = (p - 1) * (q - 1)
e = 3
d = invmod(e, phi_n)
print decrypt(encrypt(42, e, n), d, n)
m = 'qwertyuiop'.encode('hex')
c = []
for i in range(0, len(m), 2):
    c.append(encrypt(int(m[i:i+2], 16), e, n))

p = ''
for i in c:
    res = decrypt(i, d, n)
    p += chr(res)
print p
