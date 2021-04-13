"""
탈출
https://www.acmicpc.net/problem/3055
"""

import sys
from collections import deque

delta = [(-1,0), (1,0), (0,1), (0,-1)]

s = sys.stdin.readline()
R,C = map(int, s.split())

forest = []
animal = deque()
animal_v = set()
water = deque()
water_v = set()

for i in range(R):
    line = []
    s = sys.stdin.readline()
    temp = list(s.strip())

    for j in range(C):
        line.append(temp[j])
        if temp[j] == '*':
            water.append((j,i))
            water_v.add((j,i))
        if temp[j] == 'D':
            goal = (j,i)
        if temp[j] == 'S':
            animal.append((j,i))
            animal_v.add((j,i))
    forest.append(line)

flag = 0
cnt = -1
while animal:
    cnt += 1
    la = len(animal)
    lw = len(water)

    # 물번짐
    for w in range(lw):
        x,y = water.popleft()
        for dx,dy in delta:
            if 0<= x+dx <C and 0<= y+dy <R:
                if forest[y+dy][x+dx] != 'X' and forest[y+dy][x+dx] != 'D' and (x+dx, y+dy) not in water_v:
                    water_v.add((x+dx, y+dy))
                    water.append((x+dx, y+dy))

    # 고슴도치 이동
    for a in range(la):
        x,y = animal.popleft()
        if (x,y) == goal:
            flag = 1
            break

        for dx,dy in delta:
            if 0<= x+dx <C and 0<= y+dy <R:
                if forest[y+dy][x+dx] != 'X' and (x+dx, y+dy) not in water_v and (x+dx, y+dy) not in animal_v:
                    animal_v.add((x+dx, y+dy))
                    animal.append((x+dx, y+dy))
    if flag == 1:
        break


if flag == 1:
    print(cnt)
else:
    print("KAKTUS")