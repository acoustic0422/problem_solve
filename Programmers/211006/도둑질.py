"""
도둑질
https://programmers.co.kr/learn/courses/30/lessons/42897?language=python3
"""

def solution(money):
    dp = [0 for _ in range(len(money))]
    dp[0] = money[0]

    dp[1] = money[0]
    for i in range(2,len(money)):
        dp[i] = max(dp[i-1], dp[i-2]+money[i])

    cand1 = dp[-2]

    dp = [0 for _ in range(len(money))]
    dp[1] = money[1]
    for i in range(2, len(money)):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])

    cand2 = dp[-1]


    return max(cand1, cand2)

money = [1,2,3,1]
print(solution(money))