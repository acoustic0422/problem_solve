"""
연속합
https://www.acmicpc.net/problem/1912
"""
import sys
s = sys.stdin.readline()
N = int(s)

s = sys.stdin.readline()
nums = list(map(int,s.split()))

dp = [0 for _ in range(N)]
dp[0] = nums[0]

for i in range(1,N):
    dp[i] = max(dp[i-1]+nums[i], nums[i])

print(max(dp))