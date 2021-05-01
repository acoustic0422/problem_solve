"""
통계학
https://www.acmicpc.net/problem/2108
"""

import sys
from collections import defaultdict

s = sys.stdin.readline()
N = int(s)

nums = []
dic = defaultdict(int)

for _ in range(N):
    s = sys.stdin.readline()
    n = int(s)
    dic[n] += 1
    nums.append(n)

nums.sort()

avg = round(sum(nums) / len(nums))
median = nums[len(nums)//2]
dist = nums[-1] - nums[0]

sorted_dic = list(dic.items())
sorted_dic.sort(key=lambda item: (item[1], item[0]))

max_freq = sorted_dic[-1][1]

temp_list = []

for t in sorted_dic:
    if t[1] == max_freq:
        temp_list.append(t)

if len(temp_list) == 1:
    freq = temp_list[0][0]
elif len(temp_list) > 1:
    freq = temp_list[1][0]

print(avg)
print(median)
print(freq)
print(dist)
