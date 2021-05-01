"""
단어 정렬
https://www.acmicpc.net/problem/1181
"""

import sys

s = sys.stdin.readline()
N = int(s)

words = []
for _ in range(N):
    s = sys.stdin.readline().strip()
    words.append(s)

words = list(set(words))

words.sort(key=lambda w: (len(w), w))

for w in words:
    print(w)
