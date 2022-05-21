"""
단속카메라
https://programmers.co.kr/learn/courses/30/lessons/42884
"""

def solution(routes):
    answer = 0
    routes.sort(key=lambda x:(x[0], x[1]))
    overlap = [-30000, 30000]
    for s,e in routes:
        if s <= overlap[1] and e >= overlap[0]:
            overlap[0] = max(s, overlap[0])
            overlap[1] = min(e, overlap[1])
        else:
            answer += 1
            overlap[0] = s
            overlap[1] = e

    if overlap[0] != -30000 and overlap[1] != 30000:
        answer += 1

    return answer


routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))