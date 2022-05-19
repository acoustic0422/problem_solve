import sys
from collections import deque

sys.setrecursionlimit(111111)
input = sys.stdin.readline

N = int(input())

edges = [set() for _ in range(N+1)]

for _ in range(N):
    a, b = map(int, input().split())
    edges[a].add(b)
    edges[b].add(a)

result = []

isCycle = [False for _ in range(N+1)]
visited = [0 for _ in range(N+1)]


def dfs(curr, trace, cnt):
    visited[curr] = cnt
    trace.append(curr)
    for nn in list(edges[curr]):
        if not visited[nn]:
            dfs(nn, trace, cnt+1)
        elif nn in trace:
            if cnt - visited[nn] >= 2:
                for i in trace[trace.index(nn):]:
                    isCycle[i] = True
                return
    trace.remove(curr)
    return


def bfs(edges):
    q = deque()
    dist = [-1 for _ in range(N+1)]

    for i, isTrue in enumerate(isCycle):
        if isTrue:
            q.append(i)
            dist[i] = 0

    while q:
        curr = q.popleft()
        for node in list(edges[curr]):
            if dist[node] == -1:
                dist[node] = dist[curr] + 1
                q.append(node)
    return dist[1:]


for i in range(1, N+1):
    tr = []
    if not visited[i]:
        dfs(i, tr, 1)

result = bfs(edges)

print(*result)
