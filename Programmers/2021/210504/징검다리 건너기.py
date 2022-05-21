"""
징검다리 건너기
https://programmers.co.kr/learn/courses/30/lessons/64062?language=python3
"""

def solution(stones, k):
    answer = 200000001
    sorted_stones = sorted(stones)
    left = 0
    right = len(sorted_stones)-1
    while left <= right:
        mid = (left+right) // 2
        value = sorted_stones[mid]

        streak = 0
        flag = 0
        for s in stones:
            if s - value <= 0:
                streak += 1
                if streak == k:
                    flag = 1
                    break
            else:
                streak = 0
        if flag == 1:
            if answer > value:
                answer = value
            right = mid - 1
        else:
            left = mid + 1


    return answer


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3

print(solution(stones, k))
