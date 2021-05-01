"""
나이트의 이동
https://www.acmicpc.net/problem/7562
"""

import sys
from collections import deque

delta = [(-1,-2), (-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2)]

s = sys.stdin.readline()
T = int(s)

for tc in range(T):
    s = sys.stdin.readline()
    I = int(s)

    s = sys.stdin.readline()
    start = tuple(map(int,s.split()))

    s = sys.stdin.readline()
    goal = tuple(map(int, s.split()))

    q = deque()
    q.append(start)
    visited = set()

    cnt = -1
    flag = 0
    while q:
        cnt += 1
        l = len(q)
        for _ in range(l):
            x,y = q.popleft()
            if (x,y) == goal:
                flag = 1
                break
            for dx, dy in delta:
                if 0<=x+dx<I and 0<=y+dy<I:
                    if (x+dx, y+dy) not in visited:
                        visited.add((x+dx, y+dy))
                        q.append((x+dx, y+dy))
        if flag == 1:
            break

    if flag == 1:
        print(cnt)

