"""
설탕 배달
https://www.acmicpc.net/problem/2839
"""

N = int(input())

num_five = N // 5
cnt = 9999
for i in range(num_five+1):
    remain = N - (i * 5)
    if remain % 3 != 0:
        continue
    else:
        if cnt > (i + (remain // 3)):
            cnt = i + (remain // 3)

if cnt == 9999:
    print(-1)
else:
    print(cnt)