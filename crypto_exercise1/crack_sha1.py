import re
import hashlib
import itertools

def cal_h(string):
    hash_value = hashlib.sha1(string).hexdigest()
    return hash_value

hash1 = "67ae1a64661ac8b4494666f58c4822408dd0a3e4"
lst = [['Q', 'q'],[ 'W', 'w'],[ '%', '5'], ['8', '('],[ '=', '0'], ['I', 'i'], ['*', '+'], ['n', 'N']]
str1 = "0"*8
str3 = ""
str2 = list(str1)
for a in range(0,2):
    str2[0] = lst[0][a]
    for b in range(0,2):
        str2[1] = lst[1][b]
        for c in range(0,2):
            str2[2] = lst[2][c]
            for d in range(0,2):
                str2[3] = lst[3][d]
                for e in range(0,2):
                    str2[4] = lst[4][e]
                    for f in range(0,2):
                        str2[5] = lst[5][f]
                        for g in range(0,2):
                            str2[6] = lst[6][g]
                            for h in range(0,2):
                                str2[7] = lst[7][h]
                                newS = "".join(str2)
                                for i in itertools.permutations(newS, 8):
                                    str3 = cal_h("".join(i))
                                    if str3 == hash1:
                                        print "".join(i)
                                        exit(0)
