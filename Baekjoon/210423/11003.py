"""
최솟값 찾기
https://www.acmicpc.net/problem/11003
풀이 찾아봄...
https://wooooooak.github.io/algorithm/2018/12/03/%EB%B0%B1%EC%A4%8011003%EB%B2%88%EB%AC%B8%EC%A0%9C/
"""

import sys
from collections import deque

s = sys.stdin.readline()
N,L = map(int, s.split())

s = sys.stdin.readline()
nums = list(map(int, s.split()))

window = deque()
for i in range(N):
    # 현재 window의 마지막 값이 들어올 숫자보다 크면 pop
    # 들어올 값보다 크면 절대 최소값이 될 수 없기 때문에 제거한다.
    # 이렇게 연산을 하면 window가 정렬된 상태로 유지된다
    while window and window[-1][1] > nums[i]:
        window.pop()

    # 현재 윈도우 왼쪽에 (먼저 들어온 것)이 window 범위 밖이면 pop
    while window and i - window[0][0] >= L:
        window.popleft()

    ## 숫자를 넣어준다
    window.append((i, nums[i]))
    # 최소값을 출력한다
    print(window[0][1], end=' ')





