"""
나무자르기
https://www.acmicpc.net/problem/2805
"""

import sys

s = sys.stdin.readline()
N,M = map(int, s.split())

s = sys.stdin.readline()
trees = list(map(int, s.split()))


def tree_sum(h):
    count = 0
    for i in trees:
        if h < i:
            count += (i-h)
    return count


left = 0
right = max(trees)

cand = 0

while left <= right:
    mid = (left + right) // 2

    count = tree_sum(mid)

    if count >= M:
        cand = mid
        left = mid + 1
    else:
        right = mid - 1

print(cand)
