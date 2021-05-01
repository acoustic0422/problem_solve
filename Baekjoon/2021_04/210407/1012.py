"""
유기농 배추
https://www.acmicpc.net/problem/1012
"""

import sys
from collections import deque

delta = [(-1,0), (1,0), (0,-1), (0,1)]

s = sys.stdin.readline()
T = int(s)
for tc in range(T):
    s = sys.stdin.readline()
    M,N,K = map(int, s.split())

    plant = []
    plant_set = set()
    for i in range(K):
        s = sys.stdin.readline()
        X,Y = map(int, s.split())
        plant.append((X,Y))
        plant_set.add((X,Y))

    visited = set()
    cnt = 0

    for px, py in plant:
        if (px,py) not in visited:
            cnt += 1
            visited.add(cnt)
            q = deque()
            q.append((px,py))
            while len(q) > 0:
                x,y = q.popleft()
                for dx, dy in delta:
                    if 0<= x+dx < M and 0<= y+dy < N:
                        if (x+dx, y+dy) not in visited and (x+dx, y+dy) in plant_set:
                            visited.add((x+dx, y+dy))
                            q.append((x+dx, y+dy))

    print(cnt)




