"""
실패율
https://programmers.co.kr/learn/courses/30/lessons/42889
"""

def solution(N, stages):
    answer = []
    result = []
    stages.sort()

    idx = 0
    for max in range(1,N+1):
        while idx < len(stages) and stages[idx] < max :
            idx += 1
        entered = len(stages) - idx
        not_clear = 0
        while idx < len(stages) and stages[idx] == max:
            not_clear += 1
            idx += 1

        if entered == 0:
            result.append((0,max))
        else:
            result.append((not_clear / entered, max))

    result.sort(key=lambda x: (-x[0], x[1]))

    for r in result:
        answer.append(r[1])

    return answer


N = 4
stages = [4,4,4,4,4]
print(solution(N,stages))