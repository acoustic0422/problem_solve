def solution(board, moves):
    answer = 0

    stack = []
    for m in moves:
        m -= 1
        for i in range(len(board)):
            if board[i][m] > 0:
                doll = board[i][m]
                board[i][m] = 0
                if stack and stack[-1] == doll:
                    answer += 2
                    stack.pop()
                else:
                    stack.append(doll)
                break

    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))