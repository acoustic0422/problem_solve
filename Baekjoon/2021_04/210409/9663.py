"""
N-Queen
https://www.acmicpc.net/problem/9663
"""

import sys

s = sys.stdin.readline()
N = int(s)

result = 0

hori = [0 for _ in range(N)]
up_cross = [0 for _ in range(2*N-1)]
down_cross = [0 for _ in range(2*N-1)]

def nqueen(hori, uc, dc, cnt):
    if cnt == N:
        global result
        result += 1
        return

    for i in range(N):
        if hori[i] == 0 and uc[i+cnt] == 0 and dc[N-1+i-cnt] == 0:
            hori[i] = 1
            uc[i+cnt] = 1
            dc[N-1+i-cnt] = 1
            nqueen(hori,uc,dc,cnt+1)
            hori[i] = 0
            uc[i + cnt] = 0
            dc[N - 1 + i - cnt] = 0


nqueen(hori, up_cross, down_cross, 0)
print(result)

