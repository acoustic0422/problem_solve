def solution(new_id):
    answer = ''
    allowed = 'qwertyuiopasdfghjklzxcvbnm0123456789.-_'
    #step 1
    new_id = new_id.lower()
    #step2
    for c in new_id:
        if c in allowed:
            answer += c
    #step3
    while '..' in answer:
        answer = answer.replace("..", ".")
    #step4
    while answer and (answer[0] == '.' or answer[-1] == '.'):
        answer = answer.strip('.')

    #step5
    if answer == '':
        answer = 'a'

    #step6
    if len(answer) > 15:
        answer = answer[:15]
    while answer[-1] == '.':
        answer = answer.rstrip('.')

    #step7
    while len(answer) < 3:
        answer += answer[-1]


    return answer


print(solution("=.="))