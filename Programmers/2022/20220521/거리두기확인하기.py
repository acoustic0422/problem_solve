def solution(places):
    answer = []
    delta = [(-1,0), (0,1), (1,0), (0,-1)]
    cross = [(-1,-1), (-1,1), (1,-1), (1,1)]
    for room in places:
        isdist = True
        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':
                    # 상하좌우 확인
                    for dy,dx in delta:
                        if 0 <= i + dy < 5 and 0 <= j + dx < 5 and room[i + dy][j + dx] == 'P':
                            isdist = False
                        if 0 <= i+ 2*dy < 5 and 0 <= j+2*dx < 5 and room[i+2*dy][j+2*dx] == 'P':
                            if room[i+dy][j+dx] != 'X':
                                isdist = False
                        if not isdist:
                            break
                    # 대각선 확인
                    for dy, dx in cross:
                        if 0 <= i + dy < 5 and 0 <= j + dx < 5 and room[i + dy][j + dx] == 'P':
                            if room[i+dy][j] != 'X' or room[i][j+dx] != 'X':
                                isdist = False
                        if not isdist:
                            break
                if not isdist:
                    break
            if not isdist:
                break

        if isdist:
            answer.append(1)
        else:
            answer.append(0)

    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))