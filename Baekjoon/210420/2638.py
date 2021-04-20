"""
치즈
https://www.acmicpc.net/problem/2638
"""

import sys
from collections import deque


def count_face_air(cheeze, x, y):
    cnt = 0
    for dx, dy in delta:
        if cheeze[y+dx][x+dy] == -1:
            cnt += 1
    return cnt


delta = [(-1,0), (1,0), (0,-1), (0,1)]

s = sys.stdin.readline()
N,M = map(int, s.split())

cheeze = []
for _ in range(N):
    s = sys.stdin.readline()
    line = list(map(int, s.split()))
    cheeze.append(line)

# 공기주입 -> 치즈녹임 -> 반복

cnt = -1
air = deque()
air.append((0,0))
flag = 0
while True:
    cnt += 1

    while air:
        x,y = air.popleft()
        cheeze[y][x] = -1
        for dx, dy in delta:
            if 0<= x+dx <M and 0<= y+dy < N:
                if cheeze[y+dy][x+dx] == 0:
                    cheeze[y+dy][x+dx] = -1
                    air.append((x+dx, y+dy))

    for i in range(N):
        for j in range(M):
            if cheeze[i][j] == 1:
                flag = 1
                if count_face_air(cheeze, j, i) >= 2:
                    cheeze[i][j] = 0
                    air.append((j,i))

    if flag == 0:
        break
    flag = 0

print(cnt)
