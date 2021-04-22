"""
가장 긴 증가하는 부분 수열 2
https://www.acmicpc.net/problem/12015
"""

import sys


def binsearch(target):
    left, right = 1, len(dp)-1
    while left<=right:
        mid = (left+right)//2
        if dp[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return left


s = sys.stdin.readline()
N = int(s)

s = sys.stdin.readline()
nums = list(map(int, s.split()))

dp = [0]

for i in range(N):
    left = binsearch(nums[i])

    if left >= len(dp):
        dp.append(nums[i])
    else:
        dp[left] = nums[i]

print(len(dp)-1)
