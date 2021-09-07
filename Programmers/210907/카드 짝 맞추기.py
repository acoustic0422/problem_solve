"""
카드 짝 맞추기
https://programmers.co.kr/learn/courses/30/lessons/72415
"""

from collections import deque

delta = [(-1,0), (1,0), (0,-1), (0,1)]

def solution(board, r, c):
    answer = 0

    q = deque()
    q.append((r,c,0))
    charNow = -1
    visited = [[False for _ in range(4)] for _ in range(4)]
    visited[r][c] = True
    while q:
        y,x,move = q.popleft()
        if charNow == -1 and board[y][x] > 0:
            answer += move + 1
            move = 0
            charNow = board[y][x]
            board[y][x] = 0
            q = deque()
            visited = [[False for _ in range(4)] for _ in range(4)]
            visited[y][x] = True
        elif charNow == board[y][x]:
            answer += move + 1
            move = 0
            charNow = -1
            board[y][x] = 0
            q = deque()
            visited = [[False for _ in range(4)] for _ in range(4)]
            visited[y][x] = True

        # arrow move
        for dy,dx in delta:
            if 0 <= y+dy < 4 and 0 <= x+dx < 4 and visited[y+dy][x+dx] == False:
                visited[y+dy][x+dx] = True
                q.append((y+dy, x+dx, move+1))
        # ctrl + arrow move
        for dy, dx in delta:
            r,c = y,x
            while 0 <= r+dy < 4 and 0 <= c+dx < 4:
                r += dy
                c += dx
                if board[r][c] > 0 :
                    if visited[r][c] == False:
                        visited[r][c] = True
                        q.append((r,c,move+1))
                    break
                if visited[r][c] == False and (0 > r+dy or r+dy >= 4 or 0 > c+dx or c+dx >= 4):
                    if board[r][c] == 0:
                        visited[r][c] = True
                        q.append((r,c,move+1))
                        break

    return answer

board = [[1,6,7,4],
         [7,1,4,6],
         [8,3,2,8],
         [3,9,9,2]]
r = 1
c = 0
print(solution(board,r,c))