"""
수 정렬하기 3
https://www.acmicpc.net/problem/10989
"""

import sys
from collections import defaultdict

s = sys.stdin.readline()
N = int(s)

dic = defaultdict(int)

for _ in range(N):
    s = sys.stdin.readline()
    num = int(s)
    dic[num] += 1

list_of_num = sorted(dic.items())

for n, k in list_of_num:
    for _ in range(k):
        print(n)
