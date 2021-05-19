"""
최소비용 구하기 2
https://www.acmicpc.net/problem/11779
"""

import sys
import heapq
import math

def dijkstra(N, edges, start, end):
    cost = [(math.inf, []) for _ in range(N+1)]
    cost[start] = (0, [start])
    visited = [False for _ in range(N+1)]
    q = []
    heapq.heappush(q, cost[start])

    while q:
        curr_cost, history = heapq.heappop(q)
        curr_node = history[-1]
        if cost[curr_node][0] < curr_cost:
            continue
        visited[curr_node] = True
        for e, w in edges[curr_node]:
            if curr_cost + w < cost[e][0]:
                new_cost = curr_cost + w
                cost[e] = (new_cost, history+[e])
                heapq.heappush(q, cost[e])

    print(cost[end][0])
    print(len(cost[end][1]))
    print(*cost[end][1])


s = sys.stdin.readline()
n = int(s)

s = sys.stdin.readline()
m = int(s)

edges = [[] for _ in range(n+1)]

for _ in range(m):
    s = sys.stdin.readline()
    f,t,w = map(int,s.split())
    edges[f].append([t,w])

s = sys.stdin.readline()
start, end = map(int, s.split())

dijkstra(n,edges,start,end)
