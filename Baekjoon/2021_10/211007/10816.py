"""
숫자 카드 2
https://www.acmicpc.net/problem/10816
"""
from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

Adict = defaultdict(int)
for a in A:
    Adict[a] += 1

M = int(input())
C = list(map(int, input().split()))

for c in C:
    print(Adict[c], end=' ')




