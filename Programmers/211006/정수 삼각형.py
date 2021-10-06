"""
정수 삼각형
https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3
"""

def solution(triangle):
    dp = [[0 for _ in range(len(triangle[i]))] for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]

    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            dp[i][j] = triangle[i][j]
            if j == 0:
                dp[i][j] += dp[i-1][j]
            elif j == len(triangle[i])-1:
                dp[i][j] += dp[i-1][j-1]
            else:
                dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])
    return max(dp[-1])


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))