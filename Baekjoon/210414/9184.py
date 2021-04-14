"""
신나는 함수 실행
https://www.acmicpc.net/problem/9184
"""

import sys

table = []
for i in range(21):
    board = []
    for j in range(21):
        line = [0 for _ in range(21)]
        board.append(line)
    table.append(board)

for a in range(21):
    for b in range(21):
        for c in range(21):
            if a <= 0 or b <= 0 or c <= 0:
                table[a][b][c] = 1
            elif a < b < c:
                table[a][b][c] = table[a][b][c - 1] + table[a][b - 1][c - 1] - table[a][b - 1][c]
            else:
                table[a][b][c] = table[a - 1][b][c] + table[a - 1][b - 1][c] + table[a - 1][b][c - 1] - \
                                 table[a - 1][b - 1][c - 1]

while True:
    s = sys.stdin.readline()
    a,b,c = map(int, s.split())

    if a==-1 and b==-1 and c == -1:
        break

    if a<=0 or b<=0 or c<=0:
        result = 1
    elif a>20 or b>20 or c>20:
        result = table[20][20][20]
    else:
        result = table[a][b][c]

    print(f"w({a}, {b}, {c}) = {result}")
