"""
오큰수
https://www.acmicpc.net/problem/17298
"""

import sys

s = sys.stdin.readline()
N = int(s)

s = sys.stdin.readline()
nums = list(map(int, s.split()))

nge = [-1 for _ in range(N)]

stack = []

idx = 0
while idx < N:
    if len(stack) == 0:
        stack.append(idx)
    else:
        while stack and nums[stack[-1]] < nums[idx]:
            nge[stack[-1]] = nums[idx]
            stack.pop()
    stack.append(idx)
    idx += 1

for n in nge:
    print(n, end=' ')