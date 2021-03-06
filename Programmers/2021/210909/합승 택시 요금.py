"""
합승 택시 요금
https://programmers.co.kr/learn/courses/30/lessons/72413
"""

# 모든 node to node 최단거리구하는 것은 floyd
# O(n^3) 이지만, n <= 200 정도로 작음 ( n <= 4,000,000 )
# floyd 이후 계산은 간단하므로, floyd로

import math

def Floyd(edges, n):
    dist = [[math.inf for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0
    for e in edges:
        dist[e[0]-1][e[1]-1] = e[2]
        dist[e[1]-1][e[0]-1] = e[2]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dist[j][k] > dist[j][i] + dist[i][k]:
                    dist[j][k] = dist[j][i] + dist[i][k]
    return dist



def solution(n, s, a, b, fares):
    answer = math.inf

    dist = Floyd(fares, n)
    for t in range(n):
        answer = min(dist[s-1][t] + dist[t][b-1] + dist[t][a-1], answer)

    return answer