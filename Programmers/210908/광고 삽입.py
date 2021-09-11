"""
광고 삽입
https://programmers.co.kr/learn/courses/30/lessons/72414
"""


def hour2sec(hour_time):
    hour_time = hour_time.split(':')
    hour_time = list(map(int, hour_time))
    return hour_time[0] * 60 * 60 + hour_time[1] * 60 + hour_time[2]


def sec2hour(sec_time):
    sec = sec_time % 60
    minutes = sec_time // 60
    min = minutes % 60
    hour = minutes // 60
    result = ""
    result += str(hour).zfill(2)
    result += ":"
    result += str(min).zfill(2)
    result += ":"
    result += str(sec).zfill(2)
    return result


def solution(play_time, adv_time, logs):
    pTime = (0, hour2sec(play_time))
    aTimeLen = hour2sec(adv_time)

    view = [0 for _ in range(pTime[1] + 1)]
    for l in logs:
        # log의 시작점과 끝점에 +1 / -1 표시를 해준다
        start, end = l.split('-')
        view[hour2sec(start)] += 1
        view[hour2sec(end)] -= 1

    for i in range(1, len(view)):
        # 이전값을 다음값에 더해나가면 Log들이 전체 시청시간에 더해진다
        view[i] += view[i-1]


    maxViewLen = sum(view[:aTimeLen]) #초기 값을 설정하고
    currViewLen = maxViewLen
    answer = 0
    # 투포인터 알고리즘을 사용하여 최대값을 찾아나간다
    for i in range(1, pTime[1] - aTimeLen+1):
        currViewLen = currViewLen - view[i-1] + view[i+aTimeLen-1]
        if currViewLen > maxViewLen:
            maxViewLen = currViewLen
            answer = i

    return sec2hour(answer)


play_time = "50:00:00"
adv_time = "45:00:00"
logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
print(solution(play_time,adv_time,logs))
