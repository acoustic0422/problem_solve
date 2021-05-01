"""
사이클 게임
https://www.acmicpc.net/problem/20040
"""

def Find(parent, a):
    if parent[a] != a:
        parent[a] = Find(parent, parent[a])
        return parent[a]
    else:
        return parent[a]


def Union(parent,a,b):
    x = Find(parent,a)
    y = Find(parent,b)

    if x<y:
        parent[y] = x
    else:
        parent[x] = y


import sys

s = sys.stdin.readline()
N,M = map(int ,s.split())

parent = [i for i in range(N)]

cnt = 0
flag = 0
for j in range(M):
    s = sys.stdin.readline()
    a,b = map(int ,s.split())
    cnt += 1

    if Find(parent,a) != Find(parent,b):
        Union(parent,a,b)
    else:
        flag = 1
        break

if flag == 0:
    print(0)
else:
    print(cnt)
