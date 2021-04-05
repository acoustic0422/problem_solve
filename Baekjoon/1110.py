"""
더하기 사이클
https://www.acmicpc.net/problem/1110
"""

N = int(input())

cnt = 0
running = N
while True:
    cnt += 1
    front = running // 10
    back = running % 10
    new_back = (front + back) % 10

    running = back * 10 + new_back
    if running == N:
        break

print(cnt)