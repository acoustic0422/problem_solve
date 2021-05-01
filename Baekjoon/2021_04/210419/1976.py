"""
여행 가자
https://www.acmicpc.net/problem/1976
"""

import sys

s = sys.stdin.readline()
N = int(s)

s = sys.stdin.readline()
M = int(s)

parent = [i for i in range(N+1)]

def find_parent(parent, a):
    if parent[a] != a:
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


for i in range(N):
    s = sys.stdin.readline()
    line = list(map(int, s.split()))

    for j in range(i,N):
        if line[j] == 1:
            union_parent(parent,i+1,j+1)

s = sys.stdin.readline()
plan = list(map(int, s.split()))

flag = 0
root = find_parent(parent, plan[0])
for i in range(1,len(plan)):
    if find_parent(parent, plan[i]) != root:
        flag = 1
        break

if flag == 0:
    print('YES')
else:
    print('NO')