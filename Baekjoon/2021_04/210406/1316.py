"""
그룹 단어 체커
https://www.acmicpc.net/problem/1316
"""

N = int(input())

for _ in range(N):
    s = input()
    chars = set()
    now = '*'

    for c in s:
        if now == '*':
            now = c
            chars.add(c)
        else:
            if now != c:
                if c in chars:
                    N -= 1
                    break
                else:
                    now = c
                    chars.add(c)

print(N)
