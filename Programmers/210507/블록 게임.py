"""
블록 게임
https://programmers.co.kr/learn/courses/30/lessons/42894?language=python3
"""

from collections import deque


class Block(object):
    def __init__(self):
        self.is_good = False
        self.above_block = set()
        self.is_removed = False
        self.lu_point = []
        self.rd_point = []


def solution(board):
    answer = 0
    N = len(board)
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    block_dict = dict()
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] > 0 and visited[i][j] == 0:
                value = board[i][j]
                visited[i][j] = 1
                q = deque()
                q.append((i, j))
                min_x, min_y = j, i
                max_x, max_y = j, i
                while q:
                    y, x = q.popleft()
                    for dy, dx in delta:
                        if 0 <= x + dx < N and 0 <= y + dy < N:
                            if board[y + dy][x + dx] == value and visited[y + dy][x + dx] == 0:
                                visited[y + dy][x + dx] = 1
                                q.append((y + dy, x + dx))
                                if min_x > x + dx:
                                    min_x = x + dx
                                if min_y > y + dy:
                                    min_y = y + dy
                                if max_x < x + dx:
                                    max_x = x + dx
                                if max_y < y + dy:
                                    max_y = y + dy
                temp_block = Block()
                temp_block.lu_point.append((min_y, min_x))
                temp_block.rd_point.append((max_y, max_x))

                if max_x - min_x < max_y - min_y:  ## 세로로 김
                    if board[min_y + 1][min_x] == board[min_y + 1][min_x + 1] == value:
                        temp_block.is_good = False
                    elif board[min_y][min_x] == board[min_y][min_x + 1] == value:
                        temp_block.is_good = False
                    else:
                        temp_block.is_good = True
                        if board[min_y+1][min_x] == value: ## 왼쪽이 채워져 있는 경우
                            px = max_x
                            py = max_y
                            while py >= 0:
                                if board[py][px] > 0 and board[py][px] != value:
                                    temp_block.above_block.add(board[py][px])
                                py -= 1
                        elif board[min_y+1][min_x+1] == value: ## 오른쪽이 채워져 있는 경우
                            px = min_x
                            py = max_y
                            while py >= 0:
                                if board[py][px] > 0 and board[py][px] != value:
                                    temp_block.above_block.add(board[py][px])
                                py -= 1

                else:  ## 가로로 김
                    if board[min_y][min_x] == board[min_y][min_x + 1] == board[min_y][min_x + 2] == value:
                        temp_block.is_good = False
                    else:
                        temp_block.is_good = True
                        if board[min_y][min_x] == board[max_y][min_x] == value: ## 왼쪽이 튀어나온 경우
                            x = [min_x+1, min_x+2]
                            for px in x:
                                py = max_y
                                while py >=0:
                                    if board[py][px] > 0 and board[py][px] != value:
                                        temp_block.above_block.add(board[py][px])
                                    py -= 1
                        elif board[min_y][min_x+1] == board[max_y][min_x+1] == value: ## 가운데가 튀어나온 경우
                            x = [min_x, min_x + 2]
                            for px in x:
                                py = max_y
                                while py >= 0:
                                    if board[py][px] > 0 and board[py][px] != value:
                                        temp_block.above_block.add(board[py][px])
                                    py -= 1
                        elif board[min_y][min_x+2] == board[max_y][min_x+2] == value: ## 오른쪽이 튀어나온 경우
                            x = [min_x, min_x + 1]
                            for px in x:
                                py = max_y
                                while py >= 0:
                                    if board[py][px] > 0 and board[py][px] != value:
                                        temp_block.above_block.add(board[py][px])
                                    py -= 1

                block_dict[value] = temp_block

    while True:
        temp = answer

        for b in block_dict:
            if block_dict[b].is_removed is False and block_dict[b].is_good:
                above = block_dict[b].above_block
                flag = 0
                for a in above:
                    if not block_dict[a].is_removed:
                        flag = 1
                        break
                if flag == 0:
                    temp += 1
                    block_dict[b].is_removed = True
        if temp == answer:
            break
        else:
            answer = temp

    return answer


board = [[0,0,0,0,0,0,0,0,0,0],
 [0,0,4,0,0,0,5,0,0,0],
 [0,0,4,0,0,5,5,5,0,0],
 [0,0,4,4,0,0,0,0,0,0],
 [0,0,3,0,0,6,0,0,0,0],
 [0,3,3,3,6,6,6,0,0,0],
 [0,0,2,0,0,0,0,0,0,0],
 [0,0,2,2,2,0,0,0,0,0],
 [0,0,1,0,0,0,0,0,0,0],
 [1,1,1,0,0,0,0,0,0,0]]


print(solution(board))
