"""
[1차] 비밀지도
https://programmers.co.kr/learn/courses/30/lessons/17681
"""
def solution(n, arr1, arr2):
    answer = []

    res = []
    for a1, a2 in zip(arr1, arr2):
        temp = bin(a1 | a2)
        temp = temp[2:]
        if len(temp) < n:
            temp = '0'*(n-len(temp)) + temp
        res.append(temp)

    for r in res:
        temp = ''
        for c in r:
            if c == '1':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)

    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n,arr1,arr2))