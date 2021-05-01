"""
N과 M (3)
https://www.acmicpc.net/problem/15651
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

    for i in range(len(visited)):
        cand.append(i)
        dfs(M, cnt+1, i, visited, cand)
        cand.pop()


dfs(M,0,0, visited, [])



