"""
상범 빌딩
https://www.acmicpc.net/problem/6593
"""

import sys
from collections import deque

delta = [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)]

while True:
    s = sys.stdin.readline()
    L,R,C = map(int, s.split())

    if L == 0 and R == 0 and C == 0:
        break

    building = []

    for i in range(L):
        floor = []
        for j in range(R):
            s = sys.stdin.readline()
            line = []
            obs = list(s.strip())
            for k in range(C):
                line.append(obs[k])
                if obs[k] == 'S':
                    start = (i,j,k)
                if obs[k] == 'E':
                    end = (i,j,k)
            floor.append(line)
        building.append(floor)
        s = sys.stdin.readline()

    visited = set()
    q = deque()
    q.append(start)

    cnt = -1
    flag = 0
    while q:
        l = len(q)
        cnt += 1
        for _ in range(l):
            z,y,x = q.popleft()
            if (z,y,x) == end:
                flag = 1
                break

            for dz,dy,dx in delta:
                if 0<= x+dx <C and 0<= y+dy <R and 0<= z+dz <L:
                    if (z+dz, y+dy, x+dx) not in visited and (building[z+dz][y+dy][x+dx] == '.' or building[z+dz][y+dy][x+dx] == 'E'):
                        visited.add((z+dz, y+dy, x+dx))
                        q.append((z+dz, y+dy, x+dx))

        if flag == 1:
            break

    if flag == 1:
        print(f"Escaped in {cnt} minute(s).")
    else:
        print("Trapped!")




