from oracle import *

data = "9F0B13944841A832B2421B9EAF6D9836813EC9D944A5C8347A7CA69AA34D8DC0DF70E343C4000A2AE35874CE75E64C31"
ctext = [(int(data[i:i+2],16)) for i in range(0, len(data), 2)]
C = [ctext[:16], ctext[16:32], ctext[-16:]]
P = [[0] * 16, [0] * 16, [0] * 16]
IV = [[0] * 16, [0] * 16]

Oracle_Connect()

for i in range(2):
    for j in range(16):
        pos = 15 - j
        for k in range(pos+1, 16):
            IV[i][k] ^= j ^ (j+1)
        for k in range(256):
            print '[+] ', k
            IV[i][pos] = k
            res = Oracle_Send(IV[i][:] + C[i+1][:], 2)
            if res == 1:
                break
        P[i][pos] = C[i][pos] ^ IV[i][pos] ^ (j+1)
        print '[*] ', chr(P[i][pos])

Oracle_Disconnect()
text = ''
for i in range(2):
    for j in P[i]:
        text += chr(j)

print text
