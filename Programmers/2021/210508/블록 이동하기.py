"""
블록 이동하기
https://programmers.co.kr/learn/courses/30/lessons/60063?language=python3
"""

from collections import deque

def solution(board):
    answer = 0
    N = len(board)

    delta = [(-1,0), (1,0), (0,-1), (0,1)]

    vert = [[0 for _ in range(N-1)] for _ in range(N)]
    hori = [[0 for _ in range(N)] for _ in range(N-1)]

    q = deque()
    vert[0][0] = 1
    q.append((0,0,0)) # y,x,type(0: vert, 1: hori)

    while q:
        l = len(q)
        for _ in range(l):
            y,x,type = q.popleft()
            if type == 0 and y == N-1 and x == N-2:
                return answer
            if type == 1 and y == N-2 and x == N-1:
                return answer
            if type == 0: # vert
                for dy, dx in delta: # 상하좌우 이동
                    if 0<= x+dx < N-1 and 0 <= y+dy < N and vert[y+dy][x+dx] == 0 and board[y+dy][x+dx] == board[y+dy][x+dx+1] == 0:
                        vert[y+dy][x+dx] = 1
                        q.append((y+dy,x+dx,type))
                if x+1 < N and y+1 < N and board[y][x] == board[y][x+1] == board[y+1][x] == board[y+1][x+1] == 0:
                    ## 아래방향 회전
                    if hori[y][x+1] == 0:
                        hori[y][x+1] = 1
                        q.append((y,x+1,1))
                    if hori[y][x] == 0:
                        hori[y][x] = 1
                        q.append((y,x,1))
                if x+1 < N and y-1 >= 0 and board[y][x] == board[y][x+1] == board[y-1][x] == board[y-1][x+1] == 0:
                    ## 위방향 회전
                    if hori[y-1][x+1] == 0:
                        hori[y-1][x+1] = 1
                        q.append((y-1, x+1, 1))
                    if hori[y-1][x] == 0:
                        hori[y-1][x] = 1
                        q.append((y-1, x, 1))
            elif type == 1: #hori
                for dy, dx in delta:
                    if 0<= x+dx < N and 0<= y+dy < N-1 and hori[y+dy][x+dx] == 0 and board[y+dy][x+dx] == board[y+dy+1][x+dx] == 0:
                        hori[y+dy][x+dx] = 1
                        q.append((y+dy, x+dx, type))
                if x+1 < N and y+1 < N and board[y][x] == board[y][x+1] == board[y+1][x] == board[y+1][x+1] == 0:
                    ## 왼쪽에서 회전
                    if vert[y][x] == 0:
                        vert[y][x] = 1
                        q.append((y,x,0))
                    if vert[y+1][x] == 0:
                        vert[y+1][x] = 1
                        q.append((y+1, x, 0))
                if x - 1 >= 0 and y + 1 < N and board[y][x] == board[y][x - 1] == board[y + 1][x] == board[y + 1][x - 1] == 0:
                    ## 오른쪽에서 회전
                    if vert[y][x-1] == 0:
                        vert[y][x-1] = 1
                        q.append((y,x-1, 0))
                    if vert[y+1][x-1] == 0:
                        vert[y+1][x-1] = 1
                        q.append((y+1, x-1, 0))
        answer += 1

    return answer


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))
