"""
숫자 맞추기
https://www.acmicpc.net/problem/2494
** 정답 찾아 봄 **
"""

import sys

def circular(n):
    while n < 0:
        n += 10
    return n % 10


s = sys.stdin.readline()
N = int(s)

s = sys.stdin.readline()
start = list(map(int, list(s.strip())))

s = sys.stdin.readline()
end = list(map(int, list(s.strip())))

dp = [[1e9 for _ in range(10)] for _ in range(N+1)]
backward = [[-1 for _ in range(10)] for _ in range(N+1)]

for i in range(10):
    dp[0][i] = i

for i in range(1,N+1):
    for j in range(10):
        left = circular(end[i-1]-start[i-1]-j)
        right = circular(-left)

        if dp[i][j] > dp[i-1][j] + right:
            dp[i][j] = dp[i-1][j] + right
            backward[i][j] = j

        if dp[i][circular(j+left)] > dp[i-1][j] + left:
            dp[i][circular(j+left)] = dp[i-1][j] + left
            backward[i][circular(j+left)] = j

res = 1e9
min_shift = 0
for i in range(10):
    if res > dp[N][i]:
        res = dp[N][i]
        min_shift = i

print(res)

reconst = []
idx = N
while idx:
    if backward[idx][min_shift] == min_shift:
        reconst.append(-(dp[idx][min_shift] - dp[idx-1][min_shift]))
    else:
        reconst.append(dp[idx][min_shift] - dp[idx - 1][backward[idx][min_shift]])
    min_shift = backward[idx][min_shift]
    idx -= 1

reconst = reconst[::-1]

for i in range(len(reconst)):
    print(i+1, reconst[i])

