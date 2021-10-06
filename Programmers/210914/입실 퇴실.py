"""
입실 퇴실
https://programmers.co.kr/learn/courses/30/lessons/86048
"""

def solution(enter, leave):
    eidx = 0
    lidx = 0
    n = len(enter)

    answer = [0 for _ in range(n)]
    room = []
    while eidx < n and lidx < n:
        while eidx < n and leave[lidx] not in room:
            room.append(enter[eidx])
            eidx += 1

        while lidx < n and leave[lidx] in room:
            room.remove(leave[lidx])
            for r in room:
                answer[r-1] += 1
                answer[leave[lidx]-1] += 1
            lidx += 1

    return answer

enter = [1,3,2]
leave = [1,2,3]
print(solution(enter, leave))