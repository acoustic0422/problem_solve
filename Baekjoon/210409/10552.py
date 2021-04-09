"""
DOM
https://www.acmicpc.net/problem/10552
"""

import sys
from collections import defaultdict, deque

s = sys.stdin.readline()
N, M, P = map(int, s.split())

dic = dict()

for _ in range(N):
    s = sys.stdin.readline()
    f, h = map(int, s.split())
    if h not in dic.keys():
        dic[h] = f

visited = set()

ch = P
cnt = 0
while True:
    if ch in dic.keys() and ch not in visited:
        visited.add(ch)
        cnt += 1
        ch = dic[ch]

    elif ch in visited:
        print(-1)
        break

    elif ch not in dic.keys():
        print(cnt)
        break


