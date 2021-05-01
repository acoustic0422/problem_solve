"""
내려가기
https://www.acmicpc.net/problem/2096
"""

import sys

s = sys.stdin.readline()
N = int(s)

max_dp = [[0 for _ in range(3)] for _ in range(2)]
min_dp = [[0 for _ in range(3)] for _ in range(2)]

for _ in range(N):
    s = sys.stdin.readline()
    table = list(map(int,s.split()))

    max_dp[1][0] = table[0] + max(max_dp[0][0], max_dp[0][1])
    max_dp[1][1] = table[1] + max(max(max_dp[0][0], max_dp[0][1]), max_dp[0][2])
    max_dp[1][2] = table[2] + max(max_dp[0][1], max_dp[0][2])

    max_dp[0][0] = max_dp[1][0]
    max_dp[0][1] = max_dp[1][1]
    max_dp[0][2] = max_dp[1][2]

    min_dp[1][0] = table[0] + min(min_dp[0][0], min_dp[0][1])
    min_dp[1][1] = table[1] + min(min(min_dp[0][0], min_dp[0][1]), min_dp[0][2])
    min_dp[1][2] = table[2] + min(min_dp[0][1], min_dp[0][2])

    min_dp[0][0] = min_dp[1][0]
    min_dp[0][1] = min_dp[1][1]
    min_dp[0][2] = min_dp[1][2]

print(max(max_dp[1]), min(min_dp[1]))
