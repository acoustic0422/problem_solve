"""
징검다리
https://programmers.co.kr/learn/courses/30/lessons/43236?language=python3
"""

def is_possible(distance, rocks, n, min_dist):
    last = -1
    removed = 0
    for i in range(len(rocks)):
        if last == -1:
            gap = rocks[i]
        else:
            if i == len(rocks):
                gap = distance - rocks[-1]
            else:
                gap = rocks[i] - rocks[last]

        if gap < min_dist:
            removed += 1
        else:
            last = i
    if removed <= n:
        return True
    else:
        return False


def solution(distance, rocks, n):
    answer = 0
    rocks.sort()

    left = 1
    right = distance
    while left <= right:
        mid = (left + right) // 2
        if is_possible(distance, rocks, n, mid):
            left = mid + 1
            if answer < mid:
                answer = mid
        else:
            right = mid - 1

    return answer


distance = 2
rocks = [1]
n = 1
print(solution(distance, rocks, n))