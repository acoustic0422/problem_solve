"""
수 찾기
https://www.acmicpc.net/problem/1920
"""

import sys
input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

for c in C:
    if c in A:
        print(1)
    else:
        print(0)
