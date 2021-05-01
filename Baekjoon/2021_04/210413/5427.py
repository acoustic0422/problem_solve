"""
불
https://www.acmicpc.net/problem/5427
"""

import sys
from collections import deque

delta = [(-1,0), (1,0), (0,-1), (0,1)]

s = sys.stdin.readline()
T = int(s)

for _ in range(T):
    s = sys.stdin.readline()
    w,h = map(int, s.split())

    floor = []
    fire_q = deque()
    person = deque()
    fire_v = set()
    person_v = set()

    for i in range(h):
        s = sys.stdin.readline()
        line = []
        temp = list(s.strip())
        for j in range(w):
            line.append(temp[j])
            if temp[j] == '@':
                person.append((j,i))
                person_v.add((j,i))
            if temp[j] == '*':
                fire_q.append((j,i))
                fire_v.add((j,i))
        floor.append(line)

    flag = 0
    cnt = 0

    while person:
        cnt += 1
        lp = len(person)
        lf = len(fire_q)

        # 불 번짐
        for f in range(lf):
            x,y = fire_q.popleft()
            for dx, dy in delta:
                if 0<= x+dx <w and 0<= y+dy <h:
                    if floor[y+dy][x+dx] != '#' and (x+dx, y+dy) not in fire_v:
                        fire_v.add((x+dx, y+dy))
                        fire_q.append((x+dx, y+dy))

        # 사람 이동
        for p in range(lp):
            x,y = person.popleft()
            if x == 0 or x == w-1 or y == 0 or y == h-1:
                flag = 1
                break
            for dx,dy in delta:
                if 0<= x+dx < w and 0<= y+dy < h:
                    if floor[y+dy][x+dx] == '.' and (x+dx, y+dy) not in fire_v and (x+dx, y+dy) not in person_v:
                        person_v.add((x+dx, y+dy))
                        person.append((x+dx, y+dy))

        if flag == 1:
            break

    if flag == 1:
        print(cnt)
    else:
        print("IMPOSSIBLE")