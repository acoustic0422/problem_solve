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
    new_board = [[[] for _ in range(C + 1)] for _ in range(R + 1)]

    for i in range(1,R+1):
        for j in range(1,C+1):
            if board[i][j]:
                s,d,z = board[i][j]
                ss = s
                r,c = i,j
                if d == 1 or d == 2:
                    ss = ss % (2 * (R - 1))
                    while ss:
                        ss -= 1
                        if d == 1 and r == 1:
                            d = (d % 2) + 1
                        elif d == 2 and r == R:
                            d = (d % 2) + 1
                        dr, dc = delta[d]
                        r += dr
                elif d == 3 or d == 4:
                    ss = ss % (2 * (C - 1))
                    while ss:
                        ss -= 1
                        if d == 3 and c == C:
                            d = (d % 2) + 3
                        elif d == 4 and c == 1:
                            d = (d % 2) + 3
                        dr, dc = delta[d]
                        c += dc
                if new_board[r][c] != 0:
                    n_s, n_d, n_z = new_board[r][c]
                    if n_z < z:
                        new_board[r][c] = (s,d,z)
                else:
                    new_board[r][c] = (s,d,z)
    board = new_board

print(total_vol)