"""
11967
https://www.acmicpc.net/problem/11967
"""

import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int, input().split())

board = [[False for _ in range(N)] for _ in range(N)]
board[0][0] = True
visited = [[False for _ in range(N)] for _ in range(N)]
visited[0][0] = True

delta = [(-1,0), (1,0), (0,-1), (0,1)]

switches = dict()
for _ in range(M):
    x,y,a,b = map(int, input().split())
    if (x-1,y-1) in switches:
        switches[(x-1,y-1)].add((a-1,b-1))
    else:
        switches[(x-1,y-1)] = {(a-1,b-1)}


q = deque()
q.append((0,0))

while q:
    x, y = q.popleft()
    if (x,y) in switches:
        for a,b in switches[(x,y)]:
            board[a][b] = True
        del switches[(x,y)]
        q.clear()
        visited = [[False for _ in range(N)] for _ in range(N)]
        visited[x][y] = True
        q.append((x,y))
        continue
    else:
        for dx, dy in delta:
            if 0<= x+dx < N and 0<= y+dy < N and board[x+dx][y+dy] and not visited[x+dx][y+dy]:
                visited[x+dx][y+dy] = True
                q.append((x+dx, y+dy))

result = 0
for l in board:
    result += sum(l)

print(result)
