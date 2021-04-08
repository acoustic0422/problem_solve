"""
체스판 다시 칠하기
https://www.acmicpc.net/problem/1018
"""
import sys

s = sys.stdin.readline()
N,M = map(int, s.split())

board = []
for _ in range(N):
    s = sys.stdin.readline()
    board.append(s.strip())

min_draw = N * M

type1 = 'BWBWBWBW'
type2 = 'WBWBWBWB'

for i in range(0,N-8+1):
    for j in range(0,M-8+1):
        cnt1 = 0
        cnt2 = 0
        for n in range(0,8):
            line = board[i+n][j:j+8]
            if n % 2 == 0:
                cnt1 += sum([1 for c1, c2 in zip(line, type1) if c1!=c2])
                cnt2 += sum([1 for c1, c2 in zip(line, type2) if c1!=c2])
            else:
                cnt1 += sum([1 for c1, c2 in zip(line, type2) if c1 != c2])
                cnt2 += sum([1 for c1, c2 in zip(line, type1) if c1 != c2])

        if min_draw > cnt1:
            min_draw = cnt1
        if min_draw > cnt2:
            min_draw = cnt2

print(min_draw)