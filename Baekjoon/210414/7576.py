"""
토마토
https://www.acmicpc.net/problem/7576
"""

import sys
from collections import deque

delta = [(-1,0),(1,0),(0,-1),(0,1)]

s = sys.stdin.readline()
M,N = map(int, s.split())

box = []
tomato = set()
point = deque()
for i in range(N):
    line = []
    s = sys.stdin.readline()
    temp = list(map(int,s.split()))
    for j in range(M):
        if temp[j] == 1:
            tomato.add((j,i))
            point.append((j,i))
        line.append(temp[j])
    box.append(line)


cnt = -1
while point:
    cnt += 1
    l = len(point)
    for _ in range(l):
        x,y = point.popleft()
        for dx, dy in delta:
            if 0<=x+dx<M and 0<=y+dy<N:
                if box[y+dy][x+dx] == 0:
                    box[y+dy][x+dx] = 1
                    point.append((x+dx, y+dy))

flag = 0
for line in box:
    if 0 in line:
        print(-1)
        flag = 1
        break

if flag == 0:
    print(cnt)
