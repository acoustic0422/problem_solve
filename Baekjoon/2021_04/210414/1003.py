"""
피보나치 함수
https://www.acmicpc.net/problem/1003
"""

import sys

s = sys.stdin.readline()
T = int(s)

call_zero = [0 for _ in range(41)]
call_one = [0 for _ in range(41)]

call_zero[0] = 1
call_zero[1] = 0
call_one[0] = 0
call_one[1] = 1

for i in range(2,41):
    call_zero[i] = call_zero[i-2] + call_zero[i-1]
    call_one[i] = call_one[i-2] + call_one[i-1]

for _ in range(T):
    s = sys.stdin.readline()
    N = int(s)
    print(call_zero[N], call_one[N])