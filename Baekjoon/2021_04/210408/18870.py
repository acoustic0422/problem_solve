"""
좌표 압축
https://www.acmicpc.net/problem/18870
"""

import sys

s = sys.stdin.readline()
N = int(s)

s = sys.stdin.readline()
nums = list(map(int, s.split()))

s_nums = sorted(list(set(nums)))

cnt = 0
dic = dict()
for n in s_nums:
    dic[n] = cnt
    cnt += 1

for n in nums:
    print(dic[n], end=' ')
