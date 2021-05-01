"""
오큰수
https://www.acmicpc.net/problem/17298
"""

import sys

s = sys.stdin.readline()
N = int(s)

s = sys.stdin.readline()
line = list(map(int, s.split()))

result = [-1 for _ in range(N)]
stack = []

for i in range(len(line)):
    n = line[i]
    while stack and line[stack[-1]] < n:
        result[stack[-1]] = n
        stack.pop()
    stack.append(i)

for n in result:
    print(n, end=' ')
