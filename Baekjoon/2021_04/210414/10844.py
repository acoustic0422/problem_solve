"""
쉬운 계단 수
https://www.acmicpc.net/problem/10844
"""

import sys
s = sys.stdin.readline()
N = int(s)

# 앞자리 1 : 2 - 1개/ 9 : 8 - 1개 / 2~8 : +-1 - 7 * 2개 = 16개
# 뒷자리 0 : 1 - 1개/ 9 : 8 - 1개 / 1~8 : +-1 - 8 * 2개 = 18개

dp = []
for _ in range(10):
    line = [0 for _ in range(N+1)]
    dp.append(line)

for i in range(10):
    dp[i][1] = 1
dp[0][1] = 0

for j in range(2,N+1):
    for i in range(10):
        if i == 0:
            dp[i][j] = dp[i+1][j-1]
        elif i == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i+1][j-1]
        dp[i][j] = dp[i][j] % 1000000000

result = 0
for i in range(10):
    result += dp[i][N]

print(result % 1000000000)


