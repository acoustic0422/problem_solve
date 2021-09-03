"""
Four Squares
https://www.acmicpc.net/problem/17626
"""

import sys
import math

s = sys.stdin.readline()
N = int(s)

min_cnt = 4

def find_result(N,cnt):
    global min_cnt
    if N == 0:
        if cnt < min_cnt:
            min_cnt = cnt
        return
    if cnt >= min_cnt:
        return

    snum = int(math.sqrt(N))
    enum = int(math.sqrt(N/2))
    for i in range(snum,enum-1,-1):
        find_result(N - i*i,cnt+1)

find_result(N,0)

print(min_cnt)

