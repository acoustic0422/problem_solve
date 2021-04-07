"""
음식물 피하기
https://www.acmicpc.net/problem/1743
"""

import sys
from collections import deque

delta = [(-1,0), (1,0), (0,-1), (0,1)]

s = sys.stdin.readline()
N,M,K = map(int, s.split())

food = list()
food_set = set()
visited = set()

for _ in range(K):
    s = sys.stdin.readline()
    r,c = map(int, s.split())
    food.append((r,c))
    food_set.add((r,c))

max_cnt = -1

for r,c in food:
    if (r,c) not in visited:
        visited.add((r,c))
        q = deque()
        q.append((r,c))
        cnt = 1
        while len(q) > 0:
            y, x = q.popleft()
            for dx, dy in delta:
                if 1 <= x + dx <= M and 1 <= y + dy <= N:
                    if (y + dy, x + dx) not in visited and (y + dy, x + dx) in food_set:
                        visited.add((y + dy, x + dx))
                        q.append((y + dy, x + dx))
                        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt

print(max_cnt)
