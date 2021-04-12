"""
미로 탐색
https://www.acmicpc.net/problem/2178
"""

import sys
from collections import deque
import copy

delta = [(-1,0),(1,0),(0,-1),(0,1)]

s = sys.stdin.readline()
N,M = map(int, s.split())

miro = []
for _ in range(N):
    s = sys.stdin.readline()
    miro.append(list(s.strip()))

visited = set()
visited.add((0,0))

q = deque()
q.append((0,0))
cnt = 0

flag = 0
while q:
    cnt += 1
    l = len(q)
    for _ in range(l):
        x,y = q.popleft()

        if x == M-1 and y == N-1:
            flag = 1
            break

        for dx, dy in delta:
            if 0<= x+dx <M and 0<= y+dy <N:
                if miro[y+dy][x+dx] == '1' and (x+dx, y+dy) not in visited:
                    visited.add((x+dx, y+dy))
                    q.append((x+dx, y+dy))
    if flag == 1:
        break

print(cnt)


