"""
방의 개수
https://programmers.co.kr/learn/courses/30/lessons/49190
"""

from copy import deepcopy

def solution(arrows):
    answer = 0
    now = (0,0)
    delta = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

    visited = set()
    visited.add(now)

    for a in arrows:
        next = (now[0] + delta[a][0], now[1] + delta[a][1])
        if next in visited:
            answer += 1
        else:
            visited.add(next)
        now = deepcopy(next)

    return answer


arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
print(solution(arrows))