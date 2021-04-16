"""
전깃줄
https://www.acmicpc.net/problem/2565
"""

import sys
s = sys.stdin.readline()
N = int(s)

lines = []

for _ in range(N):
    s = sys.stdin.readline()
    f,t = map(int, s.split())
    lines.append((f,t))

lines.sort()

dp = [1 for _ in range(N)]

for i in range(1,N):
    f, t = lines[i]
    for j in range(i+1):
        if t > lines[j][1] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1

print(N - max(dp))
