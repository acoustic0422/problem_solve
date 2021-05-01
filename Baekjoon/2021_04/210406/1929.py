"""
소수 구하기
https://www.acmicpc.net/problem/1929
"""

def eratos(M,N):
    not_prime = set()
    not_prime.add(1)
    prime = []

    for i in range(2,N+1):
        if i not in not_prime:
            if i >= M:
                prime.append(i)
            for j in range(i, N+1, i):
                not_prime.add(j)
    return prime


numbers = list(map(int, input().split()))

result = eratos(numbers[0], numbers[1])

for n in result:
    print(n)
