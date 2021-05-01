"""
K번째 수
https://www.acmicpc.net/problem/1300
*** 정답찾아봄
https://claude-u.tistory.com/449
"""

N = int(input())
K = int(input())

start = 1
end = K

while start<=end:
    mid = (start + end) // 2

    temp = 0
    for i in range(1, N+1):
        temp += min(mid//i, N)

    if temp >= K:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
