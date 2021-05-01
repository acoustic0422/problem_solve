"""
스도쿠
https://www.acmicpc.net/problem/2580
"""

import sys

flag = 0

board = []
for _ in range(9):
    s = sys.stdin.readline()
    line = list(map(int, s.split()))
    board.append(line)


def back_tracking(x,y,board):
    global flag

    for i in range(y,9):
        for j in range(x,9):
            if board[i][j] == 0:
                num_set = set()
                for n in range(9):
                    num_set.add(board[i][n])
                    num_set.add(board[n][j])
                grid_x = j // 3
                grid_y = i // 3
                for n in range(3):
                    for k in range(3):
                        num_set.add(board[grid_y*3+n][grid_x*3+k])

                for num in range(1,10):
                    if num not in num_set:
                        board[i][j] = num
                        back_tracking(j,i,board)
                        board[i][j] = 0
                        if flag == 1:
                            return
                return
        x = 0

    for i in range(9):
        for j in range(9):
            print(board[i][j], end=' ')
        print('')
    flag = 1


back_tracking(0,0, board)

