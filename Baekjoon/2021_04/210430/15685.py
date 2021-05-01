"""
드래곤 커브
https://www.acmicpc.net/problem/15685
"""

import sys

dir = [(0,1), (-1,0), (0,-1), (1,0)]

def draw_gc(x,y,d,g, grid):
    directions = [d]
    grid[y][x] = 1
    grid[y+dir[d][0]][x+dir[d][1]] = 1
    end_point = (y+dir[d][0],x+dir[d][1])
    for gen in range(1,g+1):
        for dr in directions[::-1]:
            dr = (dr+1)%4
            end_point = (end_point[0] + dir[dr][0], end_point[1] + dir[dr][1])
            grid[end_point[0]][end_point[1]] = 1

        next_dr = []
        for dr in directions[::-1]:
            next_dr.append((dr+1)%4)
        directions = directions + next_dr


def count_square(grid):
    cnt = 0
    for i in range(0,100):
        for j in range(0,100):
            if grid[i][j] + grid[i+1][j] + grid[i][j+1] + grid[i+1][j+1] == 4:
                cnt += 1
    return cnt


grid = [[0 for _ in range(101)] for _ in range(101)]

s = sys.stdin.readline()
N = int(s)

for _ in range(N):
    s = sys.stdin.readline()
    x,y,d,g = map(int,s.split())
    draw_gc(x,y,d,g,grid)

print(count_square(grid))
