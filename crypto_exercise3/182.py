def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

p = 1009
q = 3643
n = p * q
phi_n = (p - 1) * (q - 1)
min_num = n
sum_e = 0
for e in range(2, phi_n):
    if(gcd(e, phi_n) == 1):
        num = (gcd(e-1, p-1) + 1) * (gcd(e-1, q-1) + 1)
        if num < min_num:
            sum_e = e
            min_num = num
        elif num == min_num:
            sum_e += e

print sum_e
