"""
부족한 금액 계산하기
https://programmers.co.kr/learn/courses/30/lessons/82612
"""

def solution(price, money, count):
    answer = 0

    if count > 1:
        total_cnt = (count * (count + 1)) // 2
    else:
        total_cnt = 1

    total_price = total_cnt * price

    if total_price > money:
        answer = total_price - money

    return answer


p = 3
m = 20
c = 4

print(solution(p,m,c))