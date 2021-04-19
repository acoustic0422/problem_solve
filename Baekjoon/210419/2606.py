"""
바이러스
https://www.acmicpc.net/problem/2606
"""

import sys

def find_parent(parent, a):
    if parent[a] != a:
        return find_parent(parent, parent[a])
    else:
        return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


s = sys.stdin.readline()
V = int(s)

s = sys.stdin.readline()
E = int(s)

parent = [i for i in range(V+1)]


for i in range(E):
    s = sys.stdin.readline()
    f,t = map(int, s.split())
    union_parent(parent, f, t)


cnt = 0
root = find_parent(parent, 1)
for num in parent:
    if find_parent(parent, num) == root:
        cnt += 1

print(cnt-1)
