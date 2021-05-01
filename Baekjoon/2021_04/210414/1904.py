"""
01타일
https://www.acmicpc.net/problem/1904
"""

import sys
s = sys.stdin.readline()
N = int(s)

dp = [0,1,2,3,5]

if N <= 4:
    print(dp[N])
else:
    cnt = N - 4
    for _ in range(cnt):
        next = dp[-1] + dp[-2]
        next = next % 15746
        dp[-2] = dp[-1]
        dp[-1] = next

    print(dp[-1])