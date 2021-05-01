"""
한수
https://www.acmicpc.net/problem/1065
"""

def check_num(num):
    digits = []
    while num != 0:
        digits.append(num%10)
        num = num // 10

    diff = -999
    for i in range(len(digits)-1):
        if diff == -999:
            diff = digits[i] - digits[i+1]
        else:
            if diff != (digits[i] - digits[i+1]):
                return False
            else:
                continue
    return True

N = int(input())

cnt = 0
for i in range(1,N+1):
    if check_num(i):
       cnt += 1

print(cnt)
