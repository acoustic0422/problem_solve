"""
집합의 표현
https://www.acmicpc.net/problem/1717
"""

import sys
sys.setrecursionlimit(10**6)
s = sys.stdin.readline()
n, m = map(int, s.split())

parent = [i for i in range(n+1)]


def find_parent(parent, a):
    if a != parent[a]:
        parent[a] = find_parent(parent, parent[a])
        return parent[a]
    else:
        return parent[a]


def union_parent(parent, a, b):
    x = find_parent(parent, a)
    y = find_parent(parent, b)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


for _ in range(m):
    s = sys.stdin.readline()
    idx, a, b = map(int, s.split())
    if idx == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent,a) == find_parent(parent,b):
            print('YES')
        else:
            print('NO')

print(parent)
