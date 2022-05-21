from collections import defaultdict

def solution(id_list, report, k):
    answer = []

    mailcnt = defaultdict(int)
    reportcnt = defaultdict(set)
    for r in report:
        a, b = r.strip().split()
        reportcnt[b].add(a)

    for user in reportcnt:
        if len(reportcnt[user]) >= k:
            for u in list(reportcnt[user]):
                mailcnt[u] += 1

    for id in id_list:
        answer.append(mailcnt[id])

    return answer