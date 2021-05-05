"""
로또의 최고 순위와 최저 순위
https://programmers.co.kr/learn/courses/30/lessons/77484
"""
def solution(lottos, win_nums):
    answer = []
    win_nums = set(win_nums)

    cnt = 0
    zero_cnt = 0
    for l in lottos:
        if l == 0:
            zero_cnt += 1
        else:
            if l in win_nums:
                cnt += 1

    if cnt < 2:
        min_ladder = 6
    else:
        min_ladder = 7 - cnt

    if cnt+zero_cnt < 2:
        max_ladder = 6
    else:
        max_ladder = 7 - (cnt+zero_cnt)

    answer.append(max_ladder)
    answer.append(min_ladder)

    return answer