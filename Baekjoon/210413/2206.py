"""
벽 부수고 이동하기
https://www.acmicpc.net/problem/2206
"""

import sys
from collections import deque

delta = [(-1,0), (1,0), (0,-1), (0,1)]

s = sys.stdin.readline()
N,M = map(int, s.split())

floor = []


visited = set()
visited.add((0,0,1))
person = deque()
person.append((0,0,1))

for _ in range(N):
    s = sys.stdin.readline()
    line = list(s.strip())
    floor.append(line)

cnt = 0
flag = 0
while person:
    cnt += 1
    l = len(person)

    for _ in range(l):
        x,y,c = person.popleft()
        if x == M-1 and y == N-1:
            flag = 1
            break
        for dx, dy in delta:
            if 0<=x+dx<M and 0<=y+dy<N:
                if floor[y+dy][x+dx] == '1' and c > 0 and (x+dx, y+dy, c-1) not in visited:
                    visited.add((x+dx,y+dy, c-1))
                    person.append((x+dx,y+dy, c-1))
                if floor[y+dy][x+dx] == '0' and (x+dx, y+dy,c) not in visited:
                    visited.add((x+dx, y+dy,c))
                    person.append((x+dx, y+dy, c))

    if flag == 1:
        break

if flag == 1:
    print(cnt)
else:
    print(-1)