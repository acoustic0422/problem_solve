"""
RGB거리
https://www.acmicpc.net/problem/1149
"""

import sys
s = sys.stdin.readline()
N = int(s)

costs = []

for _ in range(N):
    s = sys.stdin.readline()
    line = list(map(int, s.split()))
    costs.append(line)

dp = [[0 for _ in range(3)] for _ in range(N)]

dp[0][0] = costs[0][0]
dp[0][1] = costs[0][1]
dp[0][2] = costs[0][2]

for i in range(1,N):
    dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = costs[i][2] + min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[-1]))
