"""
파도반 수열
https://www.acmicpc.net/problem/9461
"""
import sys

blue = [1,1,2,4,7] # 홀수
white = [1,2,3,5,9] # 짝수

for k in range(11,101):
    if k % 2 == 1:
        idx = (k // 2) - 1
        blue.append(white[idx] + white[idx-2])
    else:
        idx = (k // 2) - 1
        white.append(blue[idx] + blue[idx-2])


s = sys.stdin.readline()
T = int(s)

for _ in range(T):
    s = sys.stdin.readline()
    N = int(s)
    if N % 2 == 1:
        print(blue[(N//2)])
    else:
        print(white[(N//2)-1])
