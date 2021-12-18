"""
후위 표기식
https://www.acmicpc.net/problem/1918
"""

mid = input().strip()

priordict = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
stack = []
result = []

for c in mid:
    if c in '+-*/()':
        if c == '(':
            stack.append(c)
        elif c != ')':
            while stack and priordict[stack[-1]] >= priordict[c]:
                result.append(stack.pop())
            stack.append(c)
        else:
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
    else:
        result.append(c)

while stack:
    result.append(stack.pop())

print(''.join(result))