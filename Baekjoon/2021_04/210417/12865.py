"""
평범한 배낭
https://www.acmicpc.net/problem/12865
"""

import sys

s = sys.stdin.readline()
N,K = map(int, s.split())

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

items = []

for _ in range(N):
    s = sys.stdin.readline()
    w,v = map(int, s.split())
    items.append((w,v))

for i in range(1,N+1):
    W,V = items[i-1]
    for j in range(K+1):
        if j >= W:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W]+V)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])
