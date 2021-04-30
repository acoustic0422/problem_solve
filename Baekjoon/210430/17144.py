"""
미세먼지 안녕!
https://www.acmicpc.net/problem/17144
"""

import sys

delta = [(-1,0), (1,0), (0,-1), (0,1)]

s = sys.stdin.readline()
R,C,T = map(int, s.split())

room = []
for _ in range(R):
    s = sys.stdin.readline()
    line = list(map(int, s.split()))
    room.append(line)

cleaner = []
for i in range(R):
    for j in range(C):
        if room[i][j] == -1:
            cleaner.append((i,j))

while T:
    T -= 1
    ### 미세먼지 확산
    nroom = [[0 for _ in range(C)] for _ in range(R)]
    for y,x in cleaner:
        nroom[y][x] = -1

    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                dust = room[i][j]
                spread = 0
                for dy, dx in delta:
                    ny = i+dy
                    nx = j+dx
                    if 0 <= nx < C and 0 <= ny < R and nroom[ny][nx] != -1:
                        nroom[ny][nx] += dust // 5
                        spread += dust // 5
                nroom[i][j] += (dust - spread)

    ### 공기청정기 가동
    ## 반시계
    py, px = cleaner[0]

    py -= 1
    while py > 0:
        nroom[py][px] = nroom[py-1][px]
        py -= 1
    while px < C - 1:
        nroom[py][px] = nroom[py][px+1]
        px += 1
    while py < cleaner[0][0]:
        nroom[py][px] = nroom[py+1][px]
        py += 1
    while px > 1:
        nroom[py][px] = nroom[py][px-1]
        px -= 1

    nroom[py][px] = 0

    ## 시계
    py, px = cleaner[1]
    py += 1
    while py < R - 1:
        nroom[py][px] = nroom[py+1][px]
        py += 1
    while px < C - 1:
        nroom[py][px] = nroom[py][px + 1]
        px += 1
    while py > cleaner[1][0]:
        nroom[py][px] = nroom[py-1][px]
        py -= 1
    while px > 1:
        nroom[py][px] = nroom[py][px-1]
        px -= 1
    nroom[py][px] = 0

    room = nroom

result = 0
for i in range(R):
    for j in range(C):
        if room[i][j] != -1:
            result += room[i][j]

print(result)
