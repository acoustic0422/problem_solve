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

    logSec = []
    for l in logs:
        start, end = l.split('-')
        logSec.append((hour2sec(start), hour2sec(end)))

    view = [0 for _ in range(pTime[1]+1)]
    for ls, le in logSec:
        view[ls] += 1
        view[le] -= 1

    for i in range(1, len(view)):
        view[i] += view[i-1]

    for i in range(1, len(view)):
        view[i] += view[i - 1]

    maxViewLen = 0
    answer = 0
    for i in range(aTimeLen-1, pTime[1]):
        if i>= aTimeLen:
            if maxViewLen < view[i] - view[i-aTimeLen]:
                maxViewLen = view[i] - view[i-aTimeLen]
                answer = i - aTimeLen + 1
        else:
            if maxViewLen < view[i]:
                maxViewLen = view[i]
                answer = i - aTimeLen + 1

    return sec2hour(answer)


play_time = "50:00:00"
adv_time = "45:00:00"
logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
print(solution(play_time,adv_time,logs))
