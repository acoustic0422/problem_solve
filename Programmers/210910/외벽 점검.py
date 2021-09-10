"""
외벽 점검
https://programmers.co.kr/learn/courses/30/lessons/60062
"""

from itertools import permutations

def solution(n, weak, dist):
    answer = 987654321

    weakPoint = weak + [w + n for w in weak]
    L = len(weak)
    dist.sort(reverse=True)
    for idx, start in enumerate(weak): # weak의 point들을 시작점으로 설정
        for p in permutations(dist):
            count = 1 # 최소1명이므로
            pos = start # weak를 시작점
            for d in p:
                pos += d # dist만큼 갈 수 있음
                if pos >= weakPoint[idx + L - 1]: # 만약 간거리가 한 cycle을 모두 커버하면
                    answer = min(answer, count) # 최저값 갱신
                else: # 그렇지 않다면
                    pos = [w for w in weakPoint if w > pos][0] # 현재위치를 현재위치기준보다 큰 weakpoint로 잡음 (weakpoint가 아니면 의미 x)
                    count += 1 # 한명더 필요해졌으므로 count 증가
                    if count >= answer:
                        break
    return -1 if answer == 987654321 else answer



n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]
print(solution(n,weak,dist))