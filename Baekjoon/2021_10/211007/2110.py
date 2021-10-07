"""
공유기 설치
https://www.acmicpc.net/problem/2110
"""

def check(H, dist, C):
    install = 1
    now = 0
    for i in range(1,len(H)):
        if H[i] - H[now] < dist:
            continue
        else:
            install += 1
            now = i

    if install >= C:
        return True
    else:
        return False


import sys
input = sys.stdin.readline

N,C = map(int, input().split())
H = []
for _ in range(N):
    H.append(int(input()))

H.sort()

left = 1
right = H[-1] - H[0]

maxDist = 0

while left <= right:
    mid = (left+right) // 2

    if check(H,mid,C):
        maxDist = mid
        left = mid + 1
    else:
        right = mid - 1

print(maxDist)
