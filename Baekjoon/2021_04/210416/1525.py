"""
퍼즐
https://www.acmicpc.net/problem/1525
"""

import sys
from collections import deque
from copy import copy


def check_aligned(board):
    status = ''.join(board)
    if status == '123456780':
        return True
    else:
        return False

delta = [(-1,0),(1,0),(0,-1),(0,1)]

board = []
for i in range(3):
    s = sys.stdin.readline()
    a,b,c = s.split()
    board.append(a)
    board.append(b)
    board.append(c)

q = deque()
q.append(board)
visited = set()
status = "".join(board)
visited.add(status)

cnt = -1
flag = 0
while q:
    cnt += 1
    l = len(q)
    for _ in range(l):
        now = q.popleft()
        if check_aligned(now):
            flag = 1
            break
        zero_idx = now.index('0')
        x = zero_idx % 3
        y = zero_idx // 3
        for dx,dy in delta:
            if 0<= x+dx <3 and 0<= y+dy <3:
                now[(y+dy)*3 + (x+dx)], now[y*3+x] = now[y*3+x], now[(y+dy)*3 + (x+dx)]
                status = "".join(now)
                if status not in visited:
                    visited.add(status)
                    q.append(copy(now))
                now[(y+dy)*3 + (x+dx)], now[y*3+x] = now[y*3+x], now[(y+dy)*3 + (x+dx)]
    if flag == 1:
        break

if flag == 1:
    print(cnt)
else:
    print(-1)