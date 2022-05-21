"""
입국심사
https://programmers.co.kr/learn/courses/30/lessons/43238?language=python3
"""

def solution(n, times):
    answer = 0
    times.sort()
    left = 1
    right = times[-1] * n
    while left <= right:
        mid = (left+right) // 2
        numman = 0
        for t in times:
            numman += mid // t

        if n <= numman:
            answer = mid
            right = mid -1
        else:
            left = mid + 1
    return answer


n = 6
times = [7,10]
print(solution(n,times))