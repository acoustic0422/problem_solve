"""
연산자 끼워넣기
https://www.acmicpc.net/problem/14888
"""

import sys

s = sys.stdin.readline()
N = int(s)

s = sys.stdin.readline()
num_list = list(map(int, s.split()))

s = sys.stdin.readline()
op_list = list(map(int, s.split()))

min_result = 1000000000
max_result = -1000000000


def calc_num(cnt, op, op_list, num_list):
    if cnt == len(num_list)-1:
        global min_result, max_result
        temp = num_list[0]
        for i in range(1, len(num_list)):
            operator = op[i-1]
            if operator == 0:
                temp += num_list[i]
            elif operator == 1:
                temp -= num_list[i]
            elif operator == 2:
                temp *= num_list[i]
            elif operator == 3:
                if temp < 0:
                    temp = -1 * temp
                    temp = temp // num_list[i]
                    temp = -1 * temp
                else:
                    temp = temp // num_list[i]
        if temp < min_result:
            min_result = temp
        if temp > max_result:
            max_result = temp
        return

    for i in range(len(op_list)):
        if op_list[i] > 0:
            op_list[i] -= 1
            op[cnt] = i
            calc_num(cnt+1, op, op_list, num_list)
            op[cnt] = -1
            op_list[i] += 1


calc_num(0,[-1 for _ in range(N-1)], op_list, num_list)

print(max_result)
print(min_result)


