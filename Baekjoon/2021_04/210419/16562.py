"""
친구비
https://www.acmicpc.net/problem/16562
"""

import sys

s = sys.stdin.readline()
N,M,k = map(int, s.split())

s = sys.stdin.readline()
cost = list(map(int, s.split()))

parent = [i for i in range(N+1)]


def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
        return parent[a]
    else:
        return parent[a]


def union_parent(parent, a, b):
    x = find_parent(parent, a)
    y = find_parent(parent, b)

    if cost[x-1] < cost[y-1]:
        parent[y] = x
    else:
        parent[x] = y


for i in range(M):
    s = sys.stdin.readline()
    f,t = map(int, s.split())
    union_parent(parent, f, t)

visited = [0 for i in range(N+1)]

total_cost = 0
for i in range(1, N+1):
    node = find_parent(parent,i)
    if visited[node] == 0:
        visited[node] = 1
        total_cost += cost[node-1]

if total_cost <= k:
    print(total_cost)
else:
    print('Oh no')
