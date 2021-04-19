"""
별자리 만들기
https://www.acmicpc.net/problem/4386
"""

import sys
import math

def find(parent, a):
    if parent[a] != a:
        parents[a] = find(parent, parent[a])
        return parent[a]
    else:
        return parent[a]


def union(parent, a, b):
    x = find(parent, a)
    y = find(parent, b)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


s = sys.stdin.readline()
N = int(s)

points = []
for i in range(N):
    s = sys.stdin.readline()
    x,y = map(float, s.split())
    points.append((x,y))

edges = []
for i in range(N):
    for j in range(i+1, N):
        dist = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
        dist = math.sqrt(dist)
        edges.append((i,j, dist))

edges.sort(key=lambda x: x[2])

parents = [i for i in range(N+1)]

total_cost = 0
cnt = 0
for f,t,w in edges:
    if find(parents,f) != find(parents, t):
        total_cost += w
        union(parents, f, t)
        cnt += 1
    if cnt == N - 1:
        break

print(f"{total_cost:.2f}")

