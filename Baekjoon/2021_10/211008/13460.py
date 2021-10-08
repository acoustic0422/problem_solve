"""
구슬 탈출 2
https://www.acmicpc.net/problem/13460
"""

from collections import deque
import sys

def moveBall(color, dy, dx, board):
    ny = color[0]
    nx = color[1]

    while board[ny+dy][nx+dx] != '#':
        ny += dy
        nx += dx
        if board[ny][nx] == 'O':
            return [0,0]
    return [ny, nx]


input = sys.stdin.readline

delta = [(-1,0), (1,0), (0,-1), (0,1)]

N, M = map(int, input().split())
board = []
for i in range(N):
    line = list(input().strip())
    for j in range(M):
        if line[j] == 'R':
            rball = (i,j)
            line[j] = '.'
        if line[j] == 'B':
            bball = (i,j)
            line[j] = '.'
    board.append(line)

visited = set()
visited.add((rball, bball))
q = deque()
q.append([rball, bball, 0])

flag = 0
answer = 0
while q:
    red, blue, cnt = q.popleft()
    if cnt >= 10:
        break
    position = (red, blue)
    for dy, dx in delta:
        if dy < 0: # 위로
            if blue[0] < red[0]:
                mapping = (1,0)
            else:
                mapping = (0,1)

        elif dy > 0: #아래로
            if blue[0] < red[0]:
                mapping = (0,1)
            else:
                mapping = (1,0)
        elif dx < 0 : #왼쪽으로
            if blue[1] < red[1]:
                mapping = (1,0)
            else:
                mapping = (0,1)
        else:
            if blue[1] < red[1]:
                mapping = (0,1)
            else:
                mapping = (1,0)

        n1 = moveBall(position[mapping[0]], dy, dx, board)
        n2 = moveBall(position[mapping[1]], dy, dx, board)

        next = [0,0,cnt+1]
        next[mapping[0]] = n1
        next[mapping[1]] = n2

        if next[1] != [0,0]:
            if next[0] == [0,0]:
                answer = next[2]
                flag = 1
                break
            if next[mapping[0]] == next[mapping[1]]:
                next[mapping[1]][0] -= dy
                next[mapping[1]][1] -= dx
            if (tuple(next[0]), tuple(next[1])) not in visited:
                visited.add((tuple(next[0]), tuple(next[1])))
                q.append(next)
    if flag == 1:
        break

if flag == 0:
    print(-1)
else:
    print(answer)