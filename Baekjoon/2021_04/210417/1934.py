"""
최소공배수
https://www.acmicpc.net/problem/1934
"""

def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

import sys

s = sys.stdin.readline()
T = int(s)

for tc in range(T):
    s = sys.stdin.readline()
    a, b = map(int,s.split())
    print(a*b // gcd(a,b))
