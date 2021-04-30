"""
낚시왕
https://www.acmicpc.net/problem/17143
"""

import sys

delta = [(0,0), (-1,0), (1,0), (0,1), (0,-1)]

s = sys.stdin.readline()
R,C,M = map(int, s.split())

board = [[0 for _ in range(C+1)] for _ in range(R+1)]

for idx in range(M):
    s = sys.stdin.readline()
    r,c,ss,d,z = map(int, s.split())
    board[r][c] = (ss,d,z)

total_vol = 0
for land in range(1,C+1):
    ## 상어 잡기
    for i in range(1,R+1):
        if board[i][land] != 0:
            ss, d, z = board[i][land]
            total_vol += z
            board[i][land] = 0
            break
    ## 상어이동
    ## s : 속도, d: 1,2,3,4 = 상,하,좌,우, z : 크기
    new_board = [[0 for _ in range(C + 1)] for _ in range(R + 1)]

    for i in range(1,R+1):
        for j in range(1,C+1):
            if board[i][j]:
                s,d,z = board[i][j]
                ss = s
                r,c = i,j
                if d == 1 or d == 2:
                    dr, dc = delta[d]
                    r = (r + ss * dr) % ((R - 1) * 2)
                    if r > R:
                        r = 2 * R - r
                        d = (d%2) + 1
                    elif r < 1:
                        r = 2 * 1 - r
                        d = (d % 2) + 1

                elif d == 3 or d == 4:
                    dr, dc = delta[d]
                    c = (c + ss * dc) % ((C-1)*2)
                    if c > C:
                        c = 2*C - c
                        d = (d%2) + 3
                    elif c < 1:
                        c = 2 * 1 - c
                        d = (d%2) + 3

                if new_board[r][c] != 0:
                    n_s, n_d, n_z = new_board[r][c]
                    if n_z < z:
                        new_board[r][c] = (s,d,z)
                else:
                    new_board[r][c] = (s,d,z)
    board = new_board

print(total_vol)