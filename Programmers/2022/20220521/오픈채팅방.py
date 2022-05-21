from collections import defaultdict

def solution(record):
    answer = []

    username = defaultdict(str)
    for r in record:
        rec = r.strip().split()
        if rec[0] == 'Enter':
            username[rec[1]] = rec[2]
        elif rec[0] == 'Leave':
            pass
        elif rec[0] == 'Change':
            username[rec[1]] = rec[2]

    for r in record:
        rec = r.strip().split()
        message = ""
        if rec[0] == 'Enter':
            message += username[rec[1]]
            message += "님이 들어왔습니다."
            answer.append(message)
        elif rec[0] == 'Leave':
            message += username[rec[1]]
            message += "님이 나갔습니다."
            answer.append(message)
        elif rec[0] == 'Change':
            pass

    return answer