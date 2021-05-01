"""
부분수열의 합
https://www.acmicpc.net/problem/1182
** 정답 찾아봄 **
"""

import sys

result = 0

def sum_subseq(idx, cnt, N, S, nums, visited):
    if cnt > 0:
        temp = 0
        for i in range(N):
            if visited[i] == 1:
                temp += nums[i]
        if temp == S:
            global result
            result += 1

    for i in range(idx, N):
        if visited[i] == 0:
            visited[i] = 1
            sum_subseq(i+1, cnt+1, N, S, nums, visited)
            visited[i] = 0



s = sys.stdin.readline()
N,S = map(int, s.split())

s = sys.stdin.readline()
nums = list(map(int, s.split()))

visited = [0 for _ in range(N)]

sum_subseq(0,0,N,S,nums,visited)

print(result)
