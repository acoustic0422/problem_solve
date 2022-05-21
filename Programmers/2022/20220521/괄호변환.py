def isRight(p):
    stack = []
    for c in p:
        if c == '(':
            stack.append(c)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True

def solution(p):
    answer = ''
    if p == '':
        return answer
    if isRight(p):
        return p

    u = ''
    v = ''
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        u += p[i]
        if cnt == 0:
            v = p[i+1:]
            break

    if not isRight(u):
        new = '('
        new += solution(v)
        new += ')'
        for c in u[1:-1]:
            if c == '(':
                new += ')'
            else:
                new += '('
        answer = new
    else:
        u += solution(v)
        answer = u

    return answer


p = ")("
print(solution(p))