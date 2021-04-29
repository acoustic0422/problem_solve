"""
2048 (Easy)
https://www.acmicpc.net/problem/12100
"""

import sys
import copy
from collections import deque


class play_game(object):
    def __init__(self, N, board):
        self.N = N
        self.board = board

    def move_board(self, dir):
        if dir == 0: # up
            merged = set()
            for j in range(self.N):
                for i in range(1,self.N):
                    k = i
                    while self.board[k-1][j] == 0 and k > 0:
                        k -= 1
                    if k != i:
                        self.board[k][j] = self.board[i][j]
                        self.board[i][j] = 0

                    if k > 0 and self.board[k-1][j] == self.board[k][j] and (k-1,j) not in merged:
                        merged.add((k-1,j))
                        self.board[k][j] = 0
                        self.board[k-1][j] *= 2
        elif dir == 1: # down
            merged = set()
            for j in range(self.N):
                for i in range(self.N-2, -1, -1):
                    k = i
                    while k < self.N - 1 and self.board[k + 1][j] == 0 :
                        k += 1
                    if k != i:
                        self.board[k][j] = self.board[i][j]
                        self.board[i][j] = 0

                    if k < self.N-1 and self.board[k + 1][j] == self.board[k][j] and (k + 1, j) not in merged:
                        merged.add((k + 1, j))
                        self.board[k][j] = 0
                        self.board[k + 1][j] *= 2
        elif dir == 2: # left
            merged = set()
            for i in range(self.N):
                for j in range(1, self.N):
                    k = j
                    while self.board[i][k - 1] == 0 and k > 0:
                        k -= 1
                    if k != j:
                        self.board[i][k] = self.board[i][j]
                        self.board[i][j] = 0

                    if k > 0 and self.board[i][k - 1] == self.board[i][k] and (i, k - 1) not in merged:
                        merged.add((i,k - 1))
                        self.board[i][k] = 0
                        self.board[i][k - 1] *= 2
        elif dir == 3: # right
            merged = set()
            for i in range(self.N):
                for j in range(self.N-2, -1, -1):
                    k = j
                    while k < self.N - 1 and self.board[i][k + 1] == 0 :
                        k += 1
                    if k != j:
                        self.board[i][k] = self.board[i][j]
                        self.board[i][j] = 0

                    if k < self.N-1 and self.board[i][k + 1] == self.board[i][k] and (i, k + 1) not in merged:
                        merged.add((i, k + 1))
                        self.board[i][k] = 0
                        self.board[i][k + 1] *= 2

def find_max(board):
    temp = []
    for b in board:
        temp.append(max(b))
    return max(temp)

s = sys.stdin.readline()
N = int(s)
board = []

for _ in range(N):
    s = sys.stdin.readline()
    line = list(map(int,s.split()))
    board.append(line)

max_result = -1

cnt = 0
q = deque()
q.append(board)
while cnt < 5:
    cnt += 1
    l = len(q)
    for _ in range(l):
        board = q.popleft()

        for dir in range(4):
            PG = play_game(N,copy.deepcopy(board))
            PG.move_board(dir)
            max_board = find_max(PG.board)
            if max_result < max_board:
                max_result = max_board

            if board != PG.board:
                q.append(copy.deepcopy(PG.board))


print(max_result)

