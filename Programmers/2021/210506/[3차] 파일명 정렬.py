"""
[3차] 파일명 정렬
https://programmers.co.kr/learn/courses/30/lessons/17686
"""


def solution(files):
    answer = []

    file_names = []

    for i in range(len(files)):
        head = ''
        number = ''
        result = []
        for c in files[i]:
            if c in '0123456789':
                if head != '':
                    result.append(head)
                    head = ''
                number += c
            else:
                if number == '':
                    head += c
                else:
                    result.append(number)
                    number = ''
                    break
        if number != '':
            result.append(number)
        result[0] = result[0].lower()
        result[1] = int(result[1])
        result.append(i)
        result.append(files[i])
        file_names.append(result)

    file_names.sort(key=lambda x: (x[0], x[1], x[2]))

    for f in file_names:
        answer.append(f[3])

    return answer


files = ['f11.txt', 'f22.txt', 'f3.txt', 'f14.TXT']
print(solution(files))
