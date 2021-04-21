"""
부분합
https://www.acmicpc.net/problem/1806
"""

import sys

s = sys.stdin.readline()
N, goal = map(int, s.split())

s = sys.stdin.readline()
line = list(map(int, s.split()))

for i in range(1,N):
    line[i] = line[i]+line[i-1]

left = 0
right = 0

min_cnt = N * N
while left <= right:
    if left == 0:
        sum_l = 0
    else:
        sum_l = line[left-1]

    temp = line[right] - sum_l
    if temp >= goal:
        if min_cnt > right - left + 1:
            min_cnt = right - left + 1
        left += 1
    else:
        right += 1

    if right >= N:
        break

if min_cnt == N * N:
    print(0)
else:
    print(min_cnt)
    

