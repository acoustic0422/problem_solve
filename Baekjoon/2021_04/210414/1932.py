"""
정수 삼각형
https://www.acmicpc.net/problem/1932
"""

import sys
s = sys.stdin.readline()
N=int(s)

nums = []
for _ in range(N):
    s = sys.stdin.readline()
    nums.append(list(map(int, s.split())))

dp = [[0 for _ in range(i+1)] for i in range(N)]
dp[0][0] = nums[0][0]

for i in range(1,N):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = nums[i][j] + dp[i-1][j]
        elif j == i:
            dp[i][j] = nums[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = nums[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[-1]))
