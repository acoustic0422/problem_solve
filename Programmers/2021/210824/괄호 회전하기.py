"""
괄호 회전하기
https://programmers.co.kr/learn/courses/30/lessons/76502
"""

def isRight(s):
    stack = []
    for c in s:
        if c in '({[':
            stack.append(c)
        elif stack and c == ')' and stack[-1] == '(':
            stack.pop()
        elif stack and c == '}' and stack[-1] == '{':
            stack.pop()
        elif stack and c == ']' and stack[-1] == '[':
            stack.pop()
        else:
            return False
    if stack:
        return False
    else:
        return True


def solution(s):
    answer = 0
    for i in range(len(s)):
        if isRight(s):
            answer += 1
        s = s[1:] + s[0]

    return answer

s = "[](){}"
print(solution(s))