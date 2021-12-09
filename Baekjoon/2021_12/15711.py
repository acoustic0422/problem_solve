"""
환상의 짝꿍
https://www.acmicpc.net/problem/15711
"""

import sys

def check(prime):
    try:
        if sosu[prime]:
            return True
        else:
            return False
    except:
        for s in sosulist:
            if prime % s == 0:
                return False
        return True


n = int(sys.stdin.readline())
sosu = [True] * (2 * pow(10, 6) + 1)
sosulist = []
sosu[0], sosu[1] = False, False
for i in range(2, len(sosu)):
    if sosu[i]:
        sosulist.append(i)
        for j in range(i * 2, len(sosu), i):
            sosu[j] = False

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    line = a + b
    if line % 2 == 0:
        if line == 2:
            print("NO")
        else:
            print("YES")
    else:
        if check(line - 2):
            print("YES")
        else:
            print("NO")


