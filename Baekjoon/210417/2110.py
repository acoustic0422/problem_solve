"""
공유기 설치
https://www.acmicpc.net/problem/2110
"""

import sys

s = sys.stdin.readline()
N,C = map(int, s.split())

houses = []
for _ in range(N):
    s = sys.stdin.readline()
    houses.append(int(s))

houses.sort()


if C == 2:
    print(houses[-1] - houses[0])
else:
    left = 1
    right = houses[-1] - houses[0]
    cand = 0
    while left <= right:
        mid = (left+right) // 2

        cnt = 1
        curr = houses[0]
        for i in range(1,len(houses)):
            if (houses[i] - curr) >= mid:
                cnt += 1
                curr = houses[i]

        if cnt >= C:
            cand = mid
            left = mid+1
        else:
            right = mid-1

    print(cand)
