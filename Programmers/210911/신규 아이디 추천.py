"""
신규 아이디 추천
https://programmers.co.kr/learn/courses/30/lessons/72410
"""
def solution(new_id):
    answer = ''

    #step 1
    new_id = new_id.lower()

    #step 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in '-_.':
            answer += c

    #step 3
    while '..' in answer:
        answer = answer.replace('..', '.')

    #step 4
    answer = answer.strip('.')

    #step 5
    if answer == "":
        answer += 'a'

    #step 6
    if len(answer) >= 16:
        answer = answer[:15]
        while answer[-1] == '.':
            answer = answer[:-1]

    #step 7
    if len(answer) <=2:
        while len(answer) < 3:
            answer += answer[-1]

    return answer


new_id = "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))