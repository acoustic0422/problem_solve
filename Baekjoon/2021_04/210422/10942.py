"""
팰린드롬?
https://www.acmicpc.net/problem/10942
"""

import sys
import pprint

s = sys.stdin.readline()
N = int(s)

s = sys.stdin.readline()
nums = list(map(int, s.split()))

dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    dp[0][i] = 1

for i in range(1,N):
    if nums[i] == nums[i-1]:
        dp[1][i] = 1

for l in range(2,N):
    for i in range(l, N):
        if dp[l-2][i-1] == 1 and nums[i] == nums[i-l]:
            dp[l][i] = 1

s = sys.stdin.readline()
M = int(s)

for _ in range(M):
    s = sys.stdin.readline()
    S,E = map(int, s.split())

    if S == E:
        print(1)
    else:
        length = E - S
        end = E - 1
        if dp[length][end] == 1:
            print(1)
        else:
            print(0)

