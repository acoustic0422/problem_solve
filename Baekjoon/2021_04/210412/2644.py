"""
촌수계산
https://www.acmicpc.net/problem/2644
"""

import sys
from collections import defaultdict, deque

s = sys.stdin.readline()
N = int(s)

s = sys.stdin.readline()
start, end = map(int, s.split())

s = sys.stdin.readline()
M = int(s)

edges = defaultdict(set)

for _ in range(M):
    s = sys.stdin.readline()
    f,t = map(int, s.split())
    edges[f].add(t)
    edges[t].add(f)


cnt = 0

q = deque()
q.append((start, 0))
visited = set()
visited.add(start)

while q:
    curr, chon = q.popleft()
    flag = 0
    for node in edges[curr]:
        if node == end:
            flag = 1
            break
        if node not in visited:
            visited.add(node)
            q.append((node, chon+1))
    if flag == 1:
        cnt = chon + 1
        break

if cnt == 0:
    print(-1)
else:
    print(cnt)