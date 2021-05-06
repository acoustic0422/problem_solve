"""
[1차] 추석 트래픽
https://programmers.co.kr/learn/courses/30/lessons/17676
"""
def solution(lines):
    answer = 0
    traffics = []
    edges = []
    for l in lines:
        date, time, duration = l.split(' ')
        ### 시간 분리
        hour, minute, sec = time.split(':')
        end_time = int(int(hour)*3600 + int(minute)*60)*1000
        sec, msec = sec.split('.')
        end_time += int(sec)*1000 + int(msec)
        duration = int(float(duration.strip('s'))*1000)
        start_time = end_time - duration + 1
        traffics.append((start_time, end_time))
        edges.append(start_time)
        edges.append(end_time)

    edges.append(0)
    edges.sort()
    traffics.sort(key=lambda x:(x[0],x[1]))

    max_cnt = -1
    for e in edges:
        cnt = 0
        if e < 0 or e >= 86400000:
            continue
        start = e
        end = e + 999
        if end >= 86400000:
            end = 86400000-1
        for t in traffics:
            if t[0] <= end and t[1] >= start:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    answer = max_cnt

    return answer

lines  =["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
print(solution(lines))