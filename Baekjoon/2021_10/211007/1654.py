"""
랜선 자르기
https://www.acmicpc.net/problem/1654
"""

import sys
input = sys.stdin.readline

K,N = map(int, input().split())
exist = []
for _ in range(K):
    exist.append(int(input()))

left = 1
right = max(exist)

maxlen = 0

while left <= right:
    mid = (left + right) // 2

    numline = 0
    for e in exist:
        numline += e // mid

    if numline >= N:
        if maxlen < mid:
            maxlen = mid
        left = mid+1
    else:
        right = mid-1

print(maxlen)