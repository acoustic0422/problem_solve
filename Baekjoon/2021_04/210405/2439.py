"""
별찍기 - 2
https://www.acmicpc.net/problem/2439
"""

N = int(input())

for i in range(N):
    for j in range(N-i-1):
        print(' ', end='')
    for k in range(i+1):
        print('*', end='')
    print()