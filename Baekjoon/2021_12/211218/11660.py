"""
구간 합 구하기 5
https://www.acmicpc.net/problem/11660
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pyo = []
for i in range(N):
    add = list(map(int, input().split()))
    pyo.append(add)

summed = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        summed[i][j] = pyo[i][j]
        if i-1 >= 0:
            summed[i][j] += summed[i-1][j]
        if j-1 >= 0:
            summed[i][j] += summed[i][j-1]
        if i-1 >=0 and j-1 >= 0:
            summed[i][j] -= summed[i-1][j-1]

for k in range(M):
    x1,y1, x2, y2 = map(int, input().split())
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1
    result = summed[x2][y2]
    if x1 -1 >= 0:
        result -= summed[x1-1][y2]
    if y1 -1 >= 0:
        result -= summed[x2][y1-1]
    if x1 -1 >= 0 and y1 -1 >= 0:
        result += summed[x1-1][y1-1]

    print(result)


