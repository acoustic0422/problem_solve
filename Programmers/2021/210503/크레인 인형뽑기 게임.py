"""
크레인 인형뽑기 게임
https://programmers.co.kr/learn/courses/30/lessons/64061
"""

def solution(board, moves):
    answer = 0

    stack = []
    for m in moves:
        m -= 1
        h = 0
        toy = -1
        while h < len(board):
            if board[h][m] != 0:
                toy = board[h][m]
                board[h][m] = 0
                break
            h += 1
        if toy != -1:
            if stack and stack[-1] == toy:
                stack.pop()
                answer += 2
            else:
                stack.append(toy)

    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board,moves))