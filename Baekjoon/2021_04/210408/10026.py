"""
적록색약
https://www.acmicpc.net/problem/10026
"""

import sys
from collections import deque


def count_num_region(region):
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cnt = 0
    visited = set()
    N = len(region)

    for i in range(N):
        for j in range(N):
            if (j,i) not in visited:
                cnt += 1
                visited.add((j,i))
                color = region[i][j]
                q = deque()
                q.append((j,i))
                while len(q) > 0:
                    x,y = q.popleft()
                    for dx, dy in delta:
                        if 0<= x+dx < N and 0<= y+dy < N:
                            if region[y+dy][x+dx] == color and (x+dx, y+dy) not in visited:
                                visited.add((x+dx, y+dy))
                                q.append((x+dx, y+dy))

    return cnt


s = sys.stdin.readline()
N = int(s)

land = []

for _ in range(N):
    s = sys.stdin.readline()
    line = list(s.strip())
    land.append(line)

print(count_num_region(land), end=' ')

for i in range(N):
    for j in range(N):
        if land[i][j] == 'R':
            land[i][j] = 'G'

print(count_num_region(land), end=' ')

