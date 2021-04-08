"""
나이순 정렬
https://www.acmicpc.net/problem/10814
"""

import sys

s = sys.stdin.readline()
N = int(s)

members = []

for _ in range(N):
    s = sys.stdin.readline().strip()
    age, name = s.split()
    members.append((int(age), name))

members.sort(key=lambda m: m[0])

for age, name in members:
    print(age, name)
