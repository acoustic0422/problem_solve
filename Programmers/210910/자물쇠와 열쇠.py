"""
자물쇠와 열쇠
https://programmers.co.kr/learn/courses/30/lessons/60059
"""

import copy

def rotateKey(key):
    M = len(key)
    temp = [[0 for _ in range(M)] for _ in range(M)]

    for i in range(M):
        for j in range(M):
            temp[j][M-i-1] = key[i][j]

    return temp


def checkValid(lock):
    N = len(lock)

    for i in range(N):
        for j in range(N):
            if lock[i][j] != 1:
                return False
    return True


def matchKeyLock(key, lock):
    M = len(key)
    N = len(lock)

    for i in range(-M+1, N+M-1):
        for j in range(-M+1, N+M-1):
            temp = copy.deepcopy(lock)
            for k in range(0, M):
                for l in range(0, M):
                    if 0<= k+i < N and 0 <= l+j < N:
                        temp[k+i][l+j] += key[k][l]
            if checkValid(temp):
                return True

    return False



def solution(key, lock):
    answer = False

    for r in range(4):
        key = rotateKey(key)
        if matchKeyLock(key,lock):
            answer = True
            break

    return answer