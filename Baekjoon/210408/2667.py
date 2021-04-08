"""
단지번호붙이기
https://www.acmicpc.net/problem/2667
"""

import sys
from collections import deque

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

s = sys.stdin.readline()
N = int(s)

ground = []

for i in range(N):
    ground.append(sys.stdin.readline().strip())

num_houses = []
visited = set()

for i in range(N):
    for j in range(N):
        if ground[i][j] == '1' and (j, i) not in visited:
            visited.add((j, i))
            cnt = 1
            q = deque()
            q.append((j, i))
            while len(q) > 0:
                x, y = q.popleft()
                for dx, dy in delta:
                    if 0 <= x + dx < N and 0 <= y + dy < N:
                        if ground[y + dy][x + dx] == '1' and (x + dx, y + dy) not in visited:
                            visited.add((x + dx, y + dy))
                            cnt += 1
                            q.append((x + dx, y + dy))

            num_houses.append(cnt)

print(len(num_houses))
num_houses.sort()
for n in num_houses:
    print(n)
