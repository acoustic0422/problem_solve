"""
등굣길
https://programmers.co.kr/learn/courses/30/lessons/42898?language=python3
"""

def solution(m, n, puddles):
    denum = 1000000007

    dp = [[0 for _ in range(m)] for _ in range(n)]
    for x,y in puddles:
        dp[y-1][x-1] = -1

    for i in range(n):
        if dp[i][0] == -1:
            break
        else:
            dp[i][0] = 1

    for j in range(m):
        if dp[0][j] == -1:
            break
        else:
            dp[0][j] = 1

    for i in range(1,n):
        for j in range(1,m):
            if dp[i][j] >= 0:
                if dp[i-1][j] >= 0:
                    dp[i][j] += dp[i-1][j]
                if dp[i][j-1] >= 0:
                    dp[i][j] += dp[i][j-1]
                dp[i][j] %= denum
    return dp[n-1][m-1]


m = 4
n = 3
puddles = [[1,2],[2,1]]
print(solution(m,n,puddles))