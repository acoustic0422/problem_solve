"""
2636
https://www.acmicpc.net/problem/2636
"""

import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int, input().split())
cheese = []

for _ in range(N):
    cheese.append(list(map(int, input().split())))

delta = [(-1,0), (1,0), (0,-1), (0,1)]

temp = 0
for c in cheese:
    temp += sum(c)

q = deque()
q.append((0,0))
visited = [[False for _ in range(M)] for _ in range(N)]
visited[0][0] = True

time = 0
while temp > 0:
    result = temp
    melt = set()
    while q:
        y,x = q.popleft()
        for dy, dx in delta:
            if 0<=y+dy<N and 0<=x+dx<M and not visited[y+dy][x+dx]:
                if cheese[y+dy][x+dx] == 0:
                    q.append((y+dy, x+dx))
                elif cheese[y+dy][x+dx] == 1:
                    melt.add((y+dy,x+dx))
                visited[y+dy][x+dx] = True

    temp -= len(melt)
    for y,x in melt:
        cheese[y][x] = 0
        q.append((y,x))
    time += 1

print(time)
print(result)


