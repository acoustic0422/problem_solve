"""
MooTube (Silver)
https://www.acmicpc.net/problem/15591
"""

from collections import deque, defaultdict
import math
import sys
input = sys.stdin.readline

N,Q = map(int, input().split())

edges = defaultdict(list)

for _ in range(N-1):
    p, q, r = map(int, input().split())
    edges[p].append((q,r))
    edges[q].append((p,r))

for _ in range(Q):
    k,v = map(int, input().split())
    visited = [False for _ in range(N+1)]
    visited[v] = True
    q = deque()
    q.append((v,math.inf))

    answer = 0
    while q:
        now, cost = q.popleft()
        if cost >= k and cost != math.inf:
            answer += 1
        for nn, nc in edges[now]:
            if not visited[nn]:
                visited[nn] = True
                if cost > nc:
                    q.append((nn, nc))
                else:
                    q.append((nn, cost))

    print(answer)

