"""
특정한 최단 경로
https://www.acmicpc.net/problem/1504
"""

import math
import sys
import heapq

INF = sys.maxsize

def dijkstra(start, edges):
    min_cost = [INF for _ in range(N+1)]
    min_cost[start] = 0
    pq = []
    heapq.heappush(pq, (min_cost[start], start))

    while pq:
        cost, curr = heapq.heappop(pq)
        if min_cost[curr] < cost:
            continue

        if curr in edges:
            for e in edges[curr]:
                if min_cost[e] > edges[curr][e] + min_cost[curr]:
                    min_cost[e] = edges[curr][e] + min_cost[curr]
                    heapq.heappush(pq, (min_cost[e], e))

    return min_cost


s = sys.stdin.readline()
N,E = map(int, s.split())

edges = dict()
for _ in range(E):
    s = sys.stdin.readline()
    a,b,c = map(int, s.split())
    if a not in edges:
        edges[a] = dict()
    if b not in edges[a]:
        edges[a][b] = c
    else:
        if edges[a][b] > c:
            edges[a][b] = c

    if b not in edges:
        edges[b] = dict()
    if a not in edges[b]:
        edges[b][a] = c
    else:
        if edges[b][a] > c:
            edges[b][a] = c

s = sys.stdin.readline()
v1,v2 = map(int,s.split())

start = dijkstra(1,edges)
v1_ = dijkstra(v1,edges)
v2_ = dijkstra(v2, edges)

cnt = min(start[v1]+v1_[v2]+v2_[N], start[v2]+v2_[v1]+v1_[N])

if cnt < INF:
    print(cnt)
else:
    print(-1)
