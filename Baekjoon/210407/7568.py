"""
덩치
https://www.acmicpc.net/problem/7568
"""

body = []

N = int(input())

for _ in range(N):
    x,y = map(int, input().split())
    body.append([x,y])


for i in range(len(body)):
    px, py = body[i]
    rank = 1
    for idx, [x,y] in enumerate(body):
        if idx != i:
            if px < x and py < y:
                rank+=1
    print(rank, end=' ')
