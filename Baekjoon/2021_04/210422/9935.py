"""
문자열 폭발
https://www.acmicpc.net/problem/9935
"""

import sys

s = sys.stdin.readline()
string = s.strip()

s = sys.stdin.readline()
bomb = s.strip()

stack = []

for ch in string:
    stack.append(ch)

    while stack and stack[-1] == bomb[-1] and len(stack) >= len(bomb):
        flag = 0
        for i in range(len(bomb)):
            if stack[-len(bomb)+i] != bomb[i]:
                flag = 1
                break
        if flag == 0:
            for i in range(len(bomb)):
                stack.pop()
        else:
            break

if stack:
    print("".join(stack))
else:
    print('FRULA')
