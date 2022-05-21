"""
[카카오 인턴] 키패드 누르기
https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3
"""

def solution(numbers, hand):
    answer = ''
    left_hand = [3,0]
    right_hand = [3,2]

    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            answer += 'L'
            pos = n // 3
            left_hand = [pos, 0]
        elif n == 3 or n == 6 or n == 9:
            answer += 'R'
            pos = (n // 3)  - 1
            right_hand = [pos, 2]
        else:
            if n == 0:
                pos = 3
            else:
                pos = n // 3
            left_dist = abs(left_hand[0] - pos) + abs(left_hand[1] - 1)
            right_dist = abs(right_hand[0] - pos) + abs(right_hand[1] - 1)
            if left_dist < right_dist:
                answer += 'L'
                left_hand = [pos, 1]
            elif left_dist > right_dist:
                answer += 'R'
                right_hand = [pos, 1]
            else:
                if hand == 'right':
                    answer += 'R'
                    right_hand = [pos, 1]
                else:
                    answer += 'L'
                    left_hand = [pos, 1]

    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
print(solution(numbers, hand))
