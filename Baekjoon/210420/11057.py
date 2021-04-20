"""
오르막 수
https://www.acmicpc.net/problem/11057
"""

N = int(input())

dp = [[0 for _ in range(10)] for _ in range(N)]

for i in range(10):
    dp[0][i] = 1

for i in range(1,N):
    for j in range(10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]
        dp[i][j] = dp[i][j] % 10007

print(sum(dp[N-1]) % 10007)
