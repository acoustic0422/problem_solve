"""
[3차] 압축
https://programmers.co.kr/learn/courses/30/lessons/17684
"""

def solution(msg):
    answer = []

    word_dict = dict()
    c = ord('A')
    for i in range(26):
        word_dict[chr(c)] = i+1
        c += 1

    curr_num = 27
    now = ''
    for i in range(len(msg)):
        if now + msg[i] in word_dict:
            now += msg[i]
        else:
            answer.append(word_dict[now])
            word_dict[now+msg[i]] = curr_num
            curr_num += 1
            now = msg[i]
    if now != '':
        answer.append(word_dict[now])

    return answer


msg = 'TOBEORNOTTOBEORTOBEORNOT'
print(solution(msg))