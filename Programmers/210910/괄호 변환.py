"""
괄호 변환
https://programmers.co.kr/learn/courses/30/lessons/60058
"""

def checkRight(s):
    check = []
    for c in s:
        if c == "(":
            check.append(c)
        elif c == ")":
            if check and check[-1] == "(":
                check.pop()
            else:
                return False
    if check:
        return False
    else:
        return True


def solution(p):
    if p == "":
        return ""

    check = 0
    u = ""
    v = ""
    for i in range(len(p)):
        if p[i] == '(':
            check += 1
        else:
            check -= 1
        if check == 0:
            u = p[:i+1]
            v = p[i+1:]
            break
    if checkRight(u):
        answer = u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        for c in u[1:-1]:
            if c == "(":
                answer += ")"
            else:
                answer += "("

    return answer


p = "(()())()"
print(solution(p))