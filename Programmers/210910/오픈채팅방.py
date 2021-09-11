"""
오픈채팅방
https://programmers.co.kr/learn/courses/30/lessons/42888
"""

def solution(record):
    answer = []

    userDict = dict()

    for r in record:
        r = r.split(' ')
        if r[0] == "Enter":
            userDict[r[1]] = r[2]
        elif r[0] == 'Leave':
            pass
        elif r[0] == 'Change':
            userDict[r[1]] = r[2]

    for r in record:
        r = r.split(' ')
        if r[0] == 'Enter':
            answer.append(userDict[r[1]]+"님이 들어왔습니다.")
        elif r[0] == 'Leave':
            answer.append(userDict[r[1]]+"님이 나갔습니다.")
        else:
            pass

    return answer