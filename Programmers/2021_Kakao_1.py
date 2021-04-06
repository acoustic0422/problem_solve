"""
신규 아디이 추천
https://programmers.co.kr/learn/courses/30/lessons/72410
"""

def solution(new_id):
    answer = ""

    # step 1
    new_id = new_id.lower()

    # step 2
    for c in new_id:
        if c in "abcdefghijklmnopqrstuvwxyz0123456789-_.":
            answer += c

    # step 3
    while '..' in answer:
        answer = answer.replace('..', '.')

    # step 4
    answer = answer.strip('.')

    # step 5
    if answer == "":
        answer += 'a'

    # step 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:14]

    # step 7
    if len(answer) <= 2:
        answer += answer[-1] * (3 - len(answer))

    print(answer)

    return answer