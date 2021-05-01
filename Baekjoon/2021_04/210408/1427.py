"""
소트인사이드
https://www.acmicpc.net/problem/1427
"""

import sys

s = sys.stdin.readline().strip()

s = list(s)
s.sort(reverse=True)

print("".join(s))