"""
계단 오르기
https://www.acmicpc.net/problem/2579
"""

import sys
s = sys.stdin.readline()
N = int(s)

stairs = []
for _ in range(N):
    s = sys.stdin.readline()
    score = int(s)
    stairs.append(score)

dp = [0 for _ in range(N)]

for i in range(N):
    if i == 0:
        dp[0] = stairs[0]
    elif i == 1:
        dp[1] = stairs[1] + dp[0]
    elif i == 2:
        dp[2] = stairs[2] + max(stairs[0], stairs[1])
    else:
        dp[i] = stairs[i] + max(dp[i-2], dp[i-3]+stairs[i-1])

print(dp[-1])