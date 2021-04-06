"""
하노이 탑 이동 순서
https://www.acmicpc.net/problem/11729
"""


def hanoi(order, fr, by, to, N):
    if N == 1:
        order.append([fr, to])
        return

    hanoi(order, fr, to, by, N - 1)
    order.append([fr, to])
    hanoi(order, by, fr, to, N - 1)


N = int(input())

order = []
hanoi(order, 1, 2, 3, N)

print(len(order))
for f,s in order:
    print(f,s)
