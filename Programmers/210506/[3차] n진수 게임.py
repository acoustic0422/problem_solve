"""
[3차] n진수 게임
https://programmers.co.kr/learn/courses/30/lessons/17687
"""

def solution(n, t, m, p):
    answer = ''

    NOTATION = '0123456789ABCDEF'

    total_result = ''
    total_num = t * m

    for i in range(total_num):
        num = i
        temp = ''

        temp = NOTATION[num % n] + temp
        num = num // n
        while num:
            temp = NOTATION[num % n] + temp
            num = num // n
        total_result += temp

    for i in range(p-1, total_num, m):
        answer += total_result[i]

    return answer

n = 2
t = 4
m = 2
p = 1
print(solution(n,t,m,p))
