"""
[카카오 인턴] 경주로 건설
https://programmers.co.kr/learn/courses/30/lessons/67259?language=python3
"""

from collections import deque
import math

def solution(board):
    answer = 0

    visited = [[math.inf for _ in range(len(board[0]))] for _ in range(len(board))]
    delta = [(-1,0), (1,0), (0,-1), (0,1)]

    q = deque()
    q.append((0,0,-1,0)) ## y,x,dir,cost
    visited[0][0] = 0

    while q:
        y,x,d,cost = q.popleft()
        for i in range(len(delta)):
            if 0<= x+delta[i][1] < len(board) and 0<= y+delta[i][0] < len(board) and board[y+delta[i][0]][x+delta[i][1]] != 1:
                if d == -1: # initial
                    if visited[y+delta[i][0]][x+delta[i][1]] >= cost + 100:
                        visited[y + delta[i][0]][x + delta[i][1]] = cost + 100
                        q.append((y+delta[i][0], x+delta[i][1], i, cost+100) )
                elif (d < 2 and i >= 2) or (d>=2 and i<2) : ## 꺾이는 경우
                    if visited[y + delta[i][0]][x + delta[i][1]] >= cost + 600:
                        visited[y + delta[i][0]][x + delta[i][1]] = cost + 600
                        q.append((y + delta[i][0], x + delta[i][1], i, cost + 600))
                elif (d < 2 and i < 2) or (d >=2 and i>=2) : ## 직진인 경우
                    if visited[y+delta[i][0]][x+delta[i][1]] >= cost + 100:
                        visited[y + delta[i][0]][x + delta[i][1]] = cost + 100
                        q.append((y+delta[i][0], x+delta[i][1], i, cost+100) )
    answer = visited[-1][-1]
    return answer


board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
print(solution(board))
