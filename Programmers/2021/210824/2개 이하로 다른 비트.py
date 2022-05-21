"""
2개 이하로 다른 비트
https://programmers.co.kr/learn/courses/30/lessons/77885
"""

def solution(numbers):
    answer = []

    for n in numbers:
        bin_number = list('0'+bin(n)[2:])
        idx = ''.join(bin_number).rfind('0')
        bin_number[idx] = '1'

        if n % 2 == 1:
            bin_number[idx+1] = '0'

        answer.append(int(''.join(bin_number),2))

    return answer