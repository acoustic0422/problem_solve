"""
N과 M (2)
https://www.acmicpc.net/problem/15650
"""

import sys

s = sys.stdin.readline()
N, M = map(int, s.split())

visited = [0 for _ in range(N)]


def dfs(M, cnt, idx, visited, cand):
    if cnt == M:
        for n in cand:
            print(n+1, end=' ')
        print()
        return

    for i in range(idx, len(visited)):
        if visited[i] == 0:
            visited[i] = 1
            cand.append(i)
            dfs(M, cnt+1, i, visited, cand)
            cand.pop()
            visited[i] = 0


dfs(M,0,0, visited, [])



