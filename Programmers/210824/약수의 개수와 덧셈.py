"""
약수의 개수와 덧셈
https://programmers.co.kr/learn/courses/30/lessons/77884
"""

def cntFnc(n):
    result = 0
    for i in range(1,n+1):
        if n % i == 0:
            result += 1
    if result % 2 == 0:
        return True
    else:
        return False


def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        if cntFnc(num):
            answer += num
        else:
            answer -= num
    return answer