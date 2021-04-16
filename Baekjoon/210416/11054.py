"""
가장 긴 바이토닉 부분 수열
https://www.acmicpc.net/problem/11054
"""

import sys

s = sys.stdin.readline()
N = int(s)

s = sys.stdin.readline()
A = list(map(int, s.split()))

dp_inc = [1 for _ in range(N)]
dp_dec = [1 for _ in range(N)]

for i in range(1,N):
    curr = A[i]
    for j in range(i+1):
        if dp_inc[i] < dp_inc[j]+1 and A[j] < curr:
            dp_inc[i] = dp_inc[j]+1

for i in range(N-2, -1, -1):
    curr = A[i]
    for j in range(N-1, i, -1):
        if dp_dec[i] < dp_dec[j]+1 and A[j] < curr:
            dp_dec[i] = dp_dec[j]+1

max_result = -1

for i in range(N):
    if max_result < dp_inc[i]+dp_dec[i]-1:
        max_result = dp_inc[i]+dp_dec[i]-1

print(max_result)

