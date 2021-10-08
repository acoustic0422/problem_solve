"""
가장 먼 노드
https://programmers.co.kr/learn/courses/30/lessons/49189?language=python3
"""

from collections import defaultdict, deque

def solution(n, edge):
    answer = 0

    edges = defaultdict(list)
    for f, t in edge:
        edges[f].append(t)
        edges[t].append(f)
    visited = [False for _ in range(n+1)]

    q = deque()
    q.append(1)
    visited[1] = True

    while q:
        ql = len(q)
        answer = ql
        for l in range(ql):
            node = q.popleft()
            for nn in edges[node]:
                if visited[nn] == False:
                    visited[nn] = True
                    q.append(nn)

    return answer