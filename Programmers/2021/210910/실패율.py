"""
실패율
https://programmers.co.kr/learn/courses/30/lessons/42889
"""

def solution(N, stages):
    answer = []
    result = []
    stages.sort()

    idx = 0
    for upper in range(1,N+1): # 최대 stage 1 ~ max까지
        while idx < len(stages) and stages[idx] < upper: # stage가 max보다 같거나 클때까지 이동
            idx += 1
        entered = len(stages) - idx # 현재위치부터 마지막까지는 upper stage에 도달한 것
        notClear = 0
        while idx < len(stages) and stages[idx] == upper: # 도달했으나 깨지 못한 stage 수 세기
            notClear += 1
            idx += 1

        if entered == 0: # 분모가 0이면 0 처리
            result.append((0, upper))
        else:
            result.append((notClear / entered, upper))

    result.sort(key = lambda x: (-x[0], x[1]))

    for r in result:
        answer.append(r[1])


    return answer


N = 4
stages = [4, 4, 4, 4, 4]
print(solution(N, stages))
