"""
평균
https://www.acmicpc.net/problem/1546
"""

N = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)

mean_score = 0
for s in scores:
    mean_score += s
mean_score /= len(scores)

new_mean = (mean_score / max_score) * 100

print(new_mean)

