"""
뱀과 사다리 게임
https://www.acmicpc.net/problem/16928
"""

import sys
from collections import deque

delta = [1,2,3,4,5,6]

s = sys.stdin.readline()
N,M = map(int, s.split())

ladder = dict()
snake = dict()

for _ in range(N):
    s = sys.stdin.readline()
    f, t = map(int, s.split())
    ladder[f] = t

for _ in range(M):
    s = sys.stdin.readline()
    f,t = map(int, s.split())
    snake[f] = t

q = deque()
visited = set()
q.append(1)
visited.add(1)

cnt = -1
flag = 0
while q:
    cnt += 1
    l = len(q)
    for _ in range(l):
        curr = q.popleft()
        if curr == 100:
            flag = 1
            break
        for d in delta:
            if curr+d<=100 and curr+d not in visited:
                visited.add(curr+d)
                if curr+d in ladder.keys():
                    visited.add(ladder[curr+d])
                    q.append(ladder[curr+d])
                elif curr+d in snake.keys():
                    visited.add(snake[curr+d])
                    q.append(snake[curr+d])
                else:
                    q.append(curr+d)
    if flag == 1:
        break

if flag == 1:
    print(cnt)


