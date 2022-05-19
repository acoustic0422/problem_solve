import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = []
delta = [(0,1), (1,0), (0,-1), (-1,0)]

for i in range(N):
    line = input()
    board.append(list(line.strip()))

visited = [[False for _ in range(M)] for _ in range(N)]
result = False


def check_cycle(point, n, m, k, sc, sr, v, b):
    global N,M,result, delta

    if result:
        return

    for nd in range(4):
        ny, nx = n+delta[nd][0], m+delta[nd][1]
        if 0 <= ny < N and 0 <= nx < M:
            if ny == sc and nx == sr and k >= 4:
                result = True
                return

            if b[ny][nx] == point:
                if not v[ny][nx]:
                    v[ny][nx] = True
                    check_cycle(point, ny, nx, k+1, sc, sr, v, b)
                    v[ny][nx] = False


for c in range(N):
    for r in range(M):
        if not result:
            visited[c][r] = True
            check_cycle(board[c][r], c, r, 1, c, r, visited, board)

if result:
    print('Yes')
else:
    print('No')


