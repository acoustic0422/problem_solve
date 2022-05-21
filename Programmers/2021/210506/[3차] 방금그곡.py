"""
[3차] 방금그곡
https://programmers.co.kr/learn/courses/30/lessons/17683
"""

def time_str_to_min_int(time):
    hour, min = time.split(':')
    res = int(hour)*60 + int(min)
    return res


def compare_list(m, played):
    for i in range(len(played) - len(m) + 1):
        flag = 0
        for j in range(len(m)):
            if m[j] != played[i+j]:
                flag = 1
                break
        if flag == 0:
            return True
    return False

def string_to_note_list(melody):
    mel = []
    note = ''
    for c in melody:
        if c == '#':
            note += c
            mel.append(note)
            note = ''
        else:
            if note != '':
                mel.append(note)
                note = c
            else:
                note += c
    if note != '':
        mel.append(note)

    return mel


def solution(m, musicinfos):
    answer = '(None)'
    ans_len = -1
    ans_time = time_str_to_min_int("24:00")
    for mi in musicinfos:
        start, end, name, melody = mi.split(',')
        length = time_str_to_min_int(end) - time_str_to_min_int(start)

        mel = string_to_note_list(melody)
        mm = string_to_note_list(m)

        loop = length // (len(mel))
        added = length % (len(mel))
        played = []
        while loop:
            loop -= 1
            played += mel
        for i in range(added):
            played.append(mel[i])

        if compare_list(mm, played):
            if ans_len < length:
                ans_len = length
                ans_time = start
                answer = name
            elif ans_len == length:
                if ans_time > start:
                    ans_time = start
                    answer = name

    return answer


musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
m = "CC#BCC#BCC#BCC#B"
print(solution(m, musicinfos))
