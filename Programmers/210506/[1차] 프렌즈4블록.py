"""
[1차] 프렌즈4블록
https://programmers.co.kr/learn/courses/30/lessons/17679
"""

def solution(m, n, board):
    answer = 0
    kakao = []
    for line in board:
        kakao.append(list(line))

    while True:
        flag = 0
        check = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m-1):
            for j in range(n-1):
                if kakao[i][j] != '*' and kakao[i][j] == kakao[i][j+1] == kakao[i+1][j] == kakao[i+1][j+1]:
                    check[i][j] = check[i][j+1] = check[i+1][j] = check[i+1][j+1] = 1
                    flag = 1

        for i in range(m):
            for j in range(n):
                if check[i][j] == 1:
                    kakao[i][j] = '*'
                    answer += 1

        for j in range(n):
            for i in range(m-1, -1, -1):
                if kakao[i][j] == '*':
                    sidx = i-1
                    while sidx >=0:
                        if kakao[sidx][j] != '*':
                            kakao[i][j] = kakao[sidx][j]
                            kakao[sidx][j] = '*'
                            break
                        else:
                            sidx -= 1

        if flag == 0:
            break

    return answer

board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
m = 4
n = 5
print(solution(m,n,board))