"""
자물쇠와 열쇠
https://programmers.co.kr/learn/courses/30/lessons/60059?language=python3
"""

import copy

def rotate(M, key):
    temp = [[0 for _ in range(M)] for _ in range(M)]

    for i in range(M):
        for j in range(M):
            temp[j][M-1-i] = key[i][j]
    key = temp
    return key

def check_fit(N, lock):
    for i in range(N):
        for j in range(N):
            if lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    answer = False
    N = len(lock)
    M = len(key)

    for i in range(4):
        key = rotate(M,key)
        for i in range(-M+1, N):
            for j in range(-M+1, N):
                temp = copy.deepcopy(lock)
                flag = 0
                for ki in range(M):
                    for kj in range(M):
                        if 0 <= i+ki < N and 0 <= j+kj < N:
                            if key[ki][kj] == 1:
                                if temp[i+ki][j+kj] == 1:
                                    flag = 1
                                    break
                                elif temp[i+ki][j+kj] == 0:
                                    temp[i+ki][j+kj] = 1
                    if flag == 1:
                        break
                if flag == 0:
                    if check_fit(N, temp):
                        return True
    return answer


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key,lock))