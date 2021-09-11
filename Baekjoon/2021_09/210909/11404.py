"""
플로이드
https://www.acmicpc.net/problem/11404
"""

import math
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

edges = []
for _ in range(m):
    line = list(map(int, input().split(' ')))
    edges.append(line)

dist = [[math.inf for _ in range(n+1)] for _ in range(n+1)]

for f,t,w in edges:
    if dist[f][t] > w:
        dist[f][t] = w

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if j == k:
                dist[j][k] = 0
            elif dist[j][k] > dist[j][i] + dist[i][k]:
                dist[j][k] = dist[j][i] + dist[i][k]

for i in range(1,n+1):
    for j in range(1,n+1):
        if dist[i][j] == math.inf:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()

