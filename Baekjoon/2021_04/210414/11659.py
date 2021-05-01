"""
구간 합 구하기 4
https://www.acmicpc.net/problem/11659
"""

import sys

s = sys.stdin.readline()
N,M = map(int, s.split())

s = sys.stdin.readline()
nums = list(map(int, s.split()))

sum_results = [nums[0]]
for i in range(1,N):
    sum_results.append(sum_results[i-1] + nums[i])


for _ in range(M):
    s = sys.stdin.readline()
    i,j = map(int, s.split())
    left = sum_results[j-1]
    if i > 1:
        right = sum_results[i-2]
    else:
        right = 0
    print(left-right)

