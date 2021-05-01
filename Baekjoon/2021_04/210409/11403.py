"""
경로 찾기
https://www.acmicpc.net/problem/11403
"""

import sys
from collections import defaultdict, deque

s = sys.stdin.readline()
N = int(s)

edges = defaultdict(list)

for i in range(N):
    s = sys.stdin.readline().strip()
    line = list(s.split())
    for j in range(N):
        if line[j] == '1':
            edges[i].append(j)

visited = set()

for base, node in edges.items():
    if node:
        q = deque()
        for n in node:
            q.append(n)
            visited.add((base, n))
            while len(q) > 0:
                next = q.popleft()
                if next in edges.keys():
                    for e in edges[next]:
                        if (base,e) not in visited:
                            q.append(e)
                            visited.add((base, e))


points = list(visited)

results = [[0 for _ in range(N)] for _ in range(N)]
for p in points:
    results[p[0]][p[1]] = 1

for s in results:
    for n in s:
        print(n, end=' ')
    print()
