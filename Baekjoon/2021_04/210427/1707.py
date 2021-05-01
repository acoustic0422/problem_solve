"""
이분 그래프
https://www.acmicpc.net/problem/1707
"""

import sys
from collections import deque, defaultdict

s = sys.stdin.readline()
K = int(s)

for _ in range(K):
    s = sys.stdin.readline()
    V, E = map(int, s.split())
    edges = defaultdict(list)

    for e in range(E):
        s = sys.stdin.readline()
        f, t = map(int, s.split())
        edges[f].append(t)
        edges[t].append(f)

    is_bip = True
    visited = [0 for _ in range(V + 1)]
    q = deque()
    for i in range(1,V):
        if visited[i] == 0:
            start = 1
            visited[i] = 1
            q.append((i, 1))

            while q:
                curr, f = q.popleft()
                for e in edges[curr]:
                    if visited[e] == 0:
                        visited[e] = (f % 2) + 1
                        q.append((e, (f % 2) + 1))
                    elif visited[e] == f:
                        is_bip = False
                        break
                    elif visited[e] == (f%2) + 1:
                        continue
                if not is_bip:
                    break

    if not is_bip:
        print('NO')
    else:
        print('YES')
