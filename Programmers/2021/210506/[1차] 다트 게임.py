"""
[1차] 다트 게임
https://programmers.co.kr/learn/courses/30/lessons/17682
"""

def solution(dartResult):
    answer = 0

    get_score = []
    score = ''
    for c in dartResult:
        if c in '0123456789':
            score += c
        else:
            if score != '':
                get_score.append(int(score))
                score = ''
            if c == 'S':
                pass
            elif c == 'D':
                get_score[-1] = get_score[-1] * get_score[-1]
            elif c == 'T':
                get_score[-1] = get_score[-1] * get_score[-1] * get_score[-1]

            if c == '*':
                get_score[-1] *= 2
                if len(get_score) > 1:
                    get_score[-2] *= 2
            elif c == '#':
                get_score[-1] *= -1

    answer = sum(get_score)

    return answer