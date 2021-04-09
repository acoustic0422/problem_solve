"""
안전 영역
https://www.acmicpc.net/problem/2468
"""

import sys
from collections import defaultdict, deque

delta = [(-1,0), (1,0), (0,-1), (0,1)]

s = sys.stdin.readline()
N = int(s)

land = []
minh, maxh = 100, -1

for _ in range(N):
    s = sys.stdin.readline()
    line = list(map(int, s.split()))
    land.append(line)
    if max(line) > maxh:
        maxh = max(line)
    if min(line) < minh:
        minh = min(line)

max_region = 1

for water in range(minh, maxh):
    q = deque()
    visited = set()
    region_cnt = 0
    for i in range(N):
        for j in range(N):
            if land[i][j] > water and (j,i) not in visited:
                q.append((j,i))
                visited.add((j,i))
                region_cnt += 1
                while len(q)>0:
                    x, y = q.popleft()
                    for dx,dy in delta:
                        if 0<= x+dx <N and 0<= y+dy < N:
                            if land[y+dy][x+dx] > water and (x+dx, y+dy) not in visited:
                                q.append((x+dx, y+dy))
                                visited.add((x+dx, y+dy))

    if region_cnt > max_region:
        max_region = region_cnt

print(max_region)
