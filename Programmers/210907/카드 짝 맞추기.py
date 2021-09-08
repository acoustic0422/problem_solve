"""
카드 짝 맞추기
https://programmers.co.kr/learn/courses/30/lessons/72415
"""

from collections import deque
import copy
import math

delta = [(-1,0), (1,0), (0,-1), (0,1)]

def checkEmpty(board):
    total = 0
    for l in board:
        total += sum(l)

    if total == 0:
        return True
    else:
        return False


def matchCard(row,col,board, target):
    move = 2
    visited = [[False for _ in range(4)] for _ in range(4)]
    visited[row][col] = True
    board[row][col] = 0
    q = deque()
    q.append((row,col,move))

    while q:
        y,x,m = q.popleft()
        if board[y][x] == target:
            return y,x,m
        # arrow move
        for dy, dx in delta:
            if 0 <= y + dy < 4 and 0 <= x + dx < 4 and visited[y + dy][x + dx] == False:
                visited[y + dy][x + dx] = True
                q.append((y + dy, x + dx, m + 1))
        # ctrl + arrow move
        for dy, dx in delta:
            r, c = y, x
            while 0 <= r + dy < 4 and 0 <= c + dx < 4:
                r += dy
                c += dx
                if board[r][c] > 0:
                    if visited[r][c] == False:
                        visited[r][c] = True
                        q.append((r, c, m + 1))
                    break
                if visited[r][c] == False and (0 > r + dy or r + dy >= 4 or 0 > c + dx or c + dx >= 4):
                    if board[r][c] == 0:
                        visited[r][c] = True
                        q.append((r, c, m + 1))
                        break


def solution(board, r, c):
    answer = math.inf

    q = deque()
    q.append((r,c,0,board))

    while q:
        y,x,move,b = q.popleft()

        if checkEmpty(b):
            if answer > move:
                answer = move
            continue

        qq = deque()
        visited = [[False for _ in range(4)] for _ in range(4)]
        qq.append((y,x,move,b))
        while qq:
            yy,xx,mm,bb = qq.popleft()
            visited[yy][xx] = True
            if bb[yy][xx] > 0:
                nb = copy.deepcopy(bb)
                t = nb[yy][xx]
                nr,nc,nm = matchCard(yy,xx,nb,t)
                nb[yy][xx] = 0
                nb[nr][nc] = 0
                q.append((nr,nc,mm+nm,copy.deepcopy(nb)))

            # arrow move
            for dy, dx in delta:
                if 0 <= y + dy < 4 and 0 <= x + dx < 4 and visited[y + dy][x + dx] == False:
                    visited[y + dy][x + dx] = True
                    qq.append((y + dy, x + dx, mm + 1, bb))
            # ctrl + arrow move
            for dy, dx in delta:
                r, c = yy, xx
                while 0 <= r + dy < 4 and 0 <= c + dx < 4:
                    r += dy
                    c += dx
                    if bb[r][c] > 0:
                        if visited[r][c] == False:
                            visited[r][c] = True
                            qq.append((r, c, mm + 1, bb))
                        break
                    if visited[r][c] == False and (0 > r + dy or r + dy >= 4 or 0 > c + dx or c + dx >= 4):
                        if bb[r][c] == 0:
                            visited[r][c] = True
                            qq.append((r, c, mm + 1, b))
                            break

    return answer

board = [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]
r = 0
c = 1
print(solution(board,r,c))