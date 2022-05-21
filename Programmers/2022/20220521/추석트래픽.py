def solution(lines):
    answer = 0
    # (start, end, length)
    reqs = []
    edgetime = []
    for l in lines:
        l = l.strip().split()
        h,m,s = l[1].split(":")
        end = int(h)*60*60*1000 + int(m)*60*1000 + int(float(s)*1000)
        dur = int(float(l[2].strip('s'))*1000)
        start = max(end - dur + 1, 0)
        reqs.append((start, end, dur))
        edgetime.append(start)
        edgetime.append(end)

    edgetime.sort()
    reqs.sort(key=lambda x: (x[0], x[1]))

    for et in edgetime:
        start = et
        end = start + 1000 - 1
        cnt = 0
        for r in reqs:
            if r[0] <= end and r[1] >= start:
                cnt += 1
        answer = max(cnt, answer)

    return answer


lines = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
print(solution(lines))