from itertools import permutations


def calc(left, right, op):
    if op == '-':
        return left - right
    elif op == '+':
        return left + right
    elif op == '*':
        return left * right

def calc_with_prior(nums, ops, prior):
    for p in prior:
        new_nums = []
        new_ops = []
        new_nums.append(nums[0])
        for i in range(len(ops)):
            if ops[i] == p:
                left = new_nums.pop()
                right = nums[i+1]
                new_nums.append(calc(left, right, ops[i]))
            else:
                new_nums.append(nums[i+1])
                new_ops.append(ops[i])
        nums = new_nums
        ops = new_ops
    return nums[0]

def solution(expression):
    answer = -1
    ops = []
    numbers = []

    temp = ''
    for c in expression:
        if c in '+-*':
            numbers.append(int(temp))
            temp = ''
            ops.append(c)
        else:
            temp += c
    numbers.append(int(temp))

    op_set = list(set(ops))
    for t in permutations(op_set):
        temp = calc_with_prior(numbers, ops, t)
        if abs(temp) > answer:
            answer = abs(temp)

    return answer