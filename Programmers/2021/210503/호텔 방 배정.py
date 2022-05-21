"""
호텔 방 배정
https://programmers.co.kr/learn/courses/30/lessons/64063?language=python3
"""

def solution(k, room_number):
    answer = []

    room = dict()

    for rn in room_number:
        if rn not in room:
            room[rn] = rn + 1
            answer.append(rn)
        else:
            value = rn
            stack = []
            while value in room:
                stack.append(value)
                value = room[value]
            room[value] = value +1
            answer.append(value)
            while stack:
                node = stack.pop()
                room[node] = value

    return answer


k = 10
room_number = [1,3,4,1,3,1]
print(solution(k,room_number))