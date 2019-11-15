des = open('data.txt', 'w')
for i in range(21):
    with open('Frame'+str(i), 'r') as f:
        content = f.readline()
        n = content[0:256]
        e = content[256:2*256]
        c = content[2*256:3*256]
        des.write(n+'\n'+e+'\n'+c+'\n')
    f.close()
des.close()
