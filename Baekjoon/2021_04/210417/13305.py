"""
주유소
https://www.acmicpc.net/problem/13305
"""

import sys
s = sys.stdin.readline()
N = int(s)

s = sys.stdin.readline()
dist = list(map(int,s.split()))

s = sys.stdin.readline()
cost = list(map(int,s.split()))

result = 0
curr = cost[0]

for i in range(1,N):
    if i == N-1:
        result += curr*dist[i-1]
    else:
        result += curr * dist[i - 1]
        if curr > cost[i]:
            curr = cost[i]

print(result)
