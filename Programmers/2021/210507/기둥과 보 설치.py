"""
기둥과 보 설치
https://programmers.co.kr/learn/courses/30/lessons/60061?language=python3
"""


def check_condition(pillar, beam, x, y, type):
    if type == 0: # 기둥
        if y == 0: # 바닥위
            return True
        elif y > 0:
            if pillar[y-1][x] == 1: # 다른기둥위
                return True
            if beam[y][x] == 1 or (x-1 >=0 and beam[y][x-1] == 1): # 보의 한쪽 끝 위
                return True
            return False
    else: # 보
        if pillar[y-1][x] == 1 or (x+1 < len(pillar) and pillar[y-1][x+1] == 1):
            return True
        if x-1 >= 0 and beam[y][x-1] == 1 and x+1 < len(beam) and beam[y][x+1] == 1:
            return True
        return False



def solution(n, build_frame):
    answer = []

    pillar = [[0 for _ in range(n+1)] for _ in range(n+1)]
    beam = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for bf in build_frame:
        x,y,a,b = bf
        if b == 1: #설치
            if check_condition(pillar, beam, x, y, a):
                if a == 0: # 기둥
                    pillar[y][x] = 1
                else:
                    beam[y][x] = 1
        else: # 삭제
            if a == 0:
                pillar[y][x] = 0
                if pillar[y+1][x] == 1 and check_condition(pillar,beam, x, y+1, 0) is False:
                    pillar[y][x] = 1
                elif beam[y+1][x] == 1 and check_condition(pillar,beam, x, y+1, 1) is False:
                    pillar[y][x] = 1
                elif x-1 >= 0 and beam[y+1][x-1] == 1 and check_condition(pillar, beam, x-1, y+1, 1) is False:
                    pillar[y][x] = 1
            else:
                beam[y][x] = 0
                if x+1 <len(pillar) and pillar[y][x+1] == 1 and check_condition(pillar, beam, x+1, y, 0) is False:
                    beam[y][x] = 1
                elif pillar[y][x] == 1 and check_condition(pillar, beam, x, y, 0) is False:
                    beam[y][x] = 1
                elif x-1 >= 0 and beam[y][x-1] == 1 and check_condition(pillar, beam, x-1, y, 1) is False:
                    beam[y][x] = 1
                elif x+1 < len(beam) and beam[y][x+1] == 1 and check_condition(pillar, beam, x+1, y, 1) is False:
                    beam[y][x] = 1

    for i in range(n+1):
        for j in range(n+1):
            if pillar[i][j] == 1:
                answer.append([j,i,0])
            if beam[i][j] == 1:
                answer.append([j,i,1])

    answer.sort(key=lambda x: (x[0], x[1], x[2]))

    return answer

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build_frame))

