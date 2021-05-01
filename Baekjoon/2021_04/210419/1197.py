"""
최소 스패닝 트리
https://www.acmicpc.net/problem/1197
"""

import sys
from collections import defaultdict, deque


def Find(a):
    if p[a] == a:
        return a
    else:
        b = Find(p[a])
        p[a] = b
        return b


def Union(a,b):
    a = Find(a)
    b = Find(b)
    if a != b:
        p[b] = a


s = sys.stdin.readline()
V,E = map(int, s.split())

p = [i for i in range(V+1)]

edges = defaultdict(set)
edge_list = []
for i in range(E):
    s = sys.stdin.readline()
    f,t,w = map(int, s.split())
    edges[f].add((t,w))
    edges[t].add((f,w))
    edge_list.append((f,t,w))

edge_list.sort(key= lambda x: x[2])

result = 0
cnt = 0
for f,t,w in edge_list:
    if Find(f) != Find(t):
        Union(f,t)
        result += w
        cnt += 1
    if cnt == V-1:
        break

print(result)

