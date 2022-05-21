def solution(s):
    answer = []
    s = s[1:-1]
    sets = s.split('},{')
    elements = []
    for e in sets:
        e = e.lstrip('{').rstrip('}')
        elements.append(list(map(int, e.split(','))))

    elements.sort(key=lambda x: len(x))
    eset = set()
    for t in elements:
        for e in t:
            if e not in eset:
                answer.append(e)
                eset.add(e)

    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))