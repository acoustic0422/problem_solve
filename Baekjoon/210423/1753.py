"""
최단경로
https://www.acmicpc.net/problem/1753
다익스트라 알고리즘
"""

import sys
import heapq

INF = 1e9

s = sys.stdin.readline()
V,E = map(int, s.split())

s = sys.stdin.readline()
K = int(s)

edges = dict()

for _ in range(E):
    s = sys.stdin.readline()
    u,v,w = map(int, s.split())
    if u not in edges:
        edges[u] = dict()
    if v not in edges[u]:
        edges[u][v] = w
    else:
        if edges[u][v] > w:
            edges[u][v] = w

min_cost = [INF for _ in range(V+1)]
visited = set()
min_cost[K] = 0
heap = []
heapq.heappush(heap, (min_cost[K], K))

while heap:
    cost, curr = heapq.heappop(heap)

    # if min_cost[curr] < cost:
    #     continue
    if curr in visited:
        continue
    visited.add(curr)

    if curr in edges:
        for e in edges[curr]:
            if min_cost[e] > edges[curr][e] + min_cost[curr]:
                min_cost[e] = edges[curr][e] + min_cost[curr]
                heapq.heappush(heap, (min_cost[e], e))

for i in range(1, V+1):
    if min_cost[i] == INF:
        print('INF')
    else:
        print(min_cost[i])