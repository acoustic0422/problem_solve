"""
가장 긴 증가하는 부분 수열
https://www.acmicpc.net/problem/11053
"""

import sys

s = sys.stdin.readline()
N = int(s)

s = sys.stdin.readline()
A = list(map(int, s.split()))

dp = [1 for _ in range(N)]

for i in range(1,N):
    curr = A[i]
    for j in range(i+1):
        if dp[i] < (dp[j]+1) and A[j] < curr:
            dp[i] = dp[j]+1

print(max(dp))