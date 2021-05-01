"""
영역 구하기
https://www.acmicpc.net/problem/2583
"""

import sys
from collections import deque

delta = [(-1,0),(1,0),(0,-1),(0,1)]

s = sys.stdin.readline()
M,N,K = map(int, s.split())

region = []

for _ in range(M):
    line = []
    for _ in range(N):
        line.append('1')
    region.append(line)

for _ in range(K):
    s = sys.stdin.readline()
    x1,y1,x2,y2 = map(int, s.split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            region[y][x] = '0'

num_part = []
visited = set()

for i in range(M):
    for j in range(N):
        if region[i][j] == '1' and (j,i) not in visited:
            visited.add((j,i))
            cnt = 1
            q = deque()
            q.append((j,i))
            while len(q) > 0:
                x,y = q.popleft()
                for dx, dy in delta:
                    if 0<= x+dx < N and 0<= y+dy < M:
                        if region[y+dy][x+dx] == '1' and (x+dx, y+dy) not in visited:
                            visited.add((x+dx, y+dy))
                            cnt += 1
                            q.append((x+dx, y+dy))

            num_part.append(cnt)

num_part.sort()
print(len(num_part))
for n in num_part:
    print(n, end=' ')
