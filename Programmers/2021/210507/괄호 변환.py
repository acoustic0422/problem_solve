"""
괄호 변환
https://programmers.co.kr/learn/courses/30/lessons/60058
"""


def check_right(w):
    cnt = 0
    for c in w:
        if c == '(':
            cnt += 1
        elif c == ')':
            cnt -= 1
            if cnt < 0:
                return False
    if cnt == 0:
        return True
    else:
        return False


def solution(p):
    answer = ''
    if p == '':
        return answer

    if check_right(p) is False:
        u = ''
        idx = 0
        cnt = 0
        while idx < len(p):
            u += p[idx]
            if p[idx] == '(':
                cnt += 1
            elif p[idx] == ')':
                cnt -= 1
            idx += 1
            if cnt == 0:
                break


        v = p[idx:]

        if check_right(u):
            answer += u
            answer += solution(v)
        else:
            res = ''
            res += '('
            res += solution(v)
            res += ')'
            for i in range(1,len(u)-1):
                if u[i] == '(':
                    res += ')'
                elif u[i] == ')':
                    res += '('
            answer += res
    else:
        answer += p
    return answer


p = ')('
print(solution(p))
