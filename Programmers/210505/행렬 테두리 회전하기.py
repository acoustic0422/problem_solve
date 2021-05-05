"""
행렬 테두리 회전하기
https://programmers.co.kr/learn/courses/30/lessons/77485
"""

def turn_board(board, query):
    min_value = 10001
    x1,y1,x2,y2 = query

    xpos = x1-1
    ypos = y1-1

    temp = board[xpos][ypos]
    while xpos < x2-1:
        if board[xpos][ypos] < min_value:
            min_value = board[xpos][ypos]
        board[xpos][ypos] = board[xpos+1][ypos]
        xpos += 1

    while ypos < y2-1:
        if board[xpos][ypos] < min_value:
            min_value = board[xpos][ypos]
        board[xpos][ypos] = board[xpos][ypos+1]
        ypos += 1

    while xpos > x1-1:
        if board[xpos][ypos] < min_value:
            min_value = board[xpos][ypos]
        board[xpos][ypos] = board[xpos-1][ypos]
        xpos -= 1

    while ypos > y1-1:
        if board[xpos][ypos] < min_value:
            min_value = board[xpos][ypos]
        board[xpos][ypos] = board[xpos][ypos-1]
        ypos -= 1

    board[xpos][ypos+1] = temp

    return min_value

def solution(rows, columns, queries):
    answer = []

    board = [[i+columns*j for i in range(1,columns+1)] for j in range(rows)]

    for q in queries:
        res = turn_board(board, q)
        answer.append(res)

    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows,columns,queries))