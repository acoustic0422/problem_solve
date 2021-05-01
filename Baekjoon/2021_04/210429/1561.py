"""
놀이 공원
https://www.acmicpc.net/problem/1561
"""

import sys

s = sys.stdin.readline()
N, M = map(int, s.split())

s = sys.stdin.readline()
play = list(map(int, s.split()))

left = 0
right = N * 30
time = 0
while left <= right:
    mid = (left + right) // 2

    num_play = M
    for p in play:
        num_play += mid // p

    if num_play < N:
        left = mid + 1
    else:
        right = mid - 1
        time = mid

num_play = M
for p in play:
    num_play += (time-1) // p

for idx, p in enumerate(play):
    if time % p == 0:
        num_play += 1
    if num_play == N:
        print(idx+1)
        break