"""
상근이의 여행
https://www.acmicpc.net/problem/9372
"""

import sys

def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
        return parent[a]
    else:
        return parent[a]


def union(parent, a, b):
    x = find(parent,a)
    y = find(parent,b)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


s = sys.stdin.readline()
T = int(s)

for tc in range(T):
    s = sys.stdin.readline()
    N,M = map(int ,s.split())

    parent = [i for i in range(N+1)]

    cnt = 0
    for i in range(M):
        s = sys.stdin.readline()
        f, t = map(int, s.split())
        if find(parent, f) != find(parent, t):
            cnt += 1
            union(parent, f, t)
    print(cnt)
