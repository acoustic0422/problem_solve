"""
영화감독 숌
https://www.acmicpc.net/problem/1436
"""

import sys
s = sys.stdin.readline()
N = int(s)

cnt = 0
start_num = 666
while cnt != N:
    check_str = str(start_num)
    if '666' in check_str:
        cnt += 1
    start_num += 1

print(check_str)