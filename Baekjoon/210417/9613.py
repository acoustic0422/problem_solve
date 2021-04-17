"""
GCD 합
https://www.acmicpc.net/problem/9613
"""

import sys
import math

s = sys.stdin.readline()
T = int(s)

for tc in range(T):
    s = sys.stdin.readline()
    line = list(map(int, s.split()))

    sum_gcd = 0
    for i in range(1,line[0]+1):
        for j in range(i+1, line[0]+1):
            sum_gcd += math.gcd(line[i], line[j])

    print(sum_gcd)
