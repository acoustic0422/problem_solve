"""
DFS와 BFS
https://www.acmicpc.net/problem/1260
"""

import sys
from collections import defaultdict, deque

s = sys.stdin.readline()
N,M,V = map(int, s.split())

edges = defaultdict(set)

for _ in range(M):
    s = sys.stdin.readline()
    f, t = map(int, s.split())
    edges[f].add(t)
    edges[t].add(f)

## DFS
stack = []
stack.append(V)
visited = set()
visited.add(V)
order = [V]

while stack:
    curr = stack[-1]
    flag = 0
    for node in sorted(list(edges[curr])):
        if node not in visited:
            order.append(node)
            visited.add(node)
            stack.append(node)
            flag = 1
            break
    if flag == 0:
        stack.pop()

for i in order:
    print(i, end=' ')
print()

## BFS

q = deque()
q.append(V)
visited = set()
visited.add(V)
order = [V]

while q:
    curr = q.popleft()
    for node in sorted(list(edges[curr])):
        if node not in visited:
            visited.add(node)
            order.append(node)
            q.append(node)

for i in order:
    print(i, end=' ')