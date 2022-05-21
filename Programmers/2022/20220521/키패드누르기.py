def solution(numbers, hand):
    answer = ''
    lfinger = (3,0)
    rfinger = (3,2)

    for n in numbers:
        if n in [1,4,7]:
            answer += 'L'
            lfinger = (n//3, 0)
        elif n in [3,6,9]:
            answer += 'R'
            rfinger = (n//3-1, 2)
        elif n in [2,5,8,0]:
            if n != 0:
                ldist = abs(lfinger[0] - n//3) + abs(lfinger[1] - 1)
                rdist = abs(rfinger[0] - n//3) + abs(rfinger[1] - 1)
            else:
                ldist = abs(lfinger[0] - 3) + abs(lfinger[1] - 1)
                rdist = abs(rfinger[0] - 3) + abs(rfinger[1] - 1)

            if ldist < rdist:
                answer += 'L'
                lfinger = (3 if n==0 else n//3, 1)
            elif ldist > rdist:
                answer += 'R'
                rfinger = (3 if n==0 else n//3 , 1)
            else:
                if hand =='right':
                    answer += 'R'
                    rfinger = (3 if n==0 else n // 3, 1)
                else:
                    answer += 'L'
                    lfinger = (3 if n==0 else n // 3, 1)
    return answer


numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = 'left'
print(solution(numbers, hand))