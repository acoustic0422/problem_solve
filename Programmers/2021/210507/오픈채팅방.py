"""
오픈채팅방
https://programmers.co.kr/learn/courses/30/lessons/42888
"""


def solution(record):
    answer = []
    id_nick = dict()

    for r in record:
        temp = r.split(' ')
        if temp[0] == 'Enter':
            id_nick[temp[1]] = temp[2]
        elif temp[0] == 'Leave':
            continue
        elif temp[0] == 'Change':
            id_nick[temp[1]] = temp[2]

    for r in record:
        temp = r.split(' ')
        if temp[0] == 'Enter':
            answer.append(f"{id_nick[temp[1]]}님이 들어왔습니다.")
        elif temp[0] =='Leave':
            answer.append(f"{id_nick[temp[1]]}님이 나갔습니다.")
        else:
            continue

    return answer