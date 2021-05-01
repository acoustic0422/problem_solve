"""
책 페이지
https://www.acmicpc.net/problem/1019
정답 찾아봄...
https://nerogarret.tistory.com/36
"""

N = int(input())

result = [0 for _ in range(10)]

weight = 1
for step in range(len(str(N))):
    replaced = int(str(N//10) + '9')
    remaining = replaced - N

    for i in range(len(result)):
        result[i] += (N//10 + 1) * weight
    for i in range(10 - remaining, 10):
        result[i] -= weight

    for number in list(str(N)[:-1]):
        number = int(number)
        result[number] -= remaining * weight

    result[0] -= weight

    N //= 10
    weight *= 10

print(' '.join(map(str, result)))
