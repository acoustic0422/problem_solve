"""
매칭 점수
https://programmers.co.kr/learn/courses/30/lessons/42893
"""

class Page:
    def __init__(self):
        self.index = 0
        self.baseScore = 0
        self.linkScore = 0
        self.link = []

def solution(word, pages):
    word = word.lower()
    linkDict = dict()
    for idx, p in enumerate(pages):
        page = Page()
        temp = p.lower()
        compare = ""
        sLetters = ""
        for c in range(ord('a'), ord('z')+1):
            sLetters += chr(c)

        for c in temp:
            if c in sLetters:
                compare += c
            else:
                if word == compare:
                    page.baseScore += 1
                compare = ""

        page.index = idx

        urlStart = p.find("<head>")
        urlStart = p.find("<meta property=\"og:url\"", urlStart)
        urlStart = p.find("content=", urlStart)
        urlStart = p.find("https://", urlStart)
        urlEnd = p.find("\"",urlStart)
        url = p[urlStart:urlEnd]
        linkDict[url] = page

        start = 0
        while True:
            start = p.find('<a href=', start)
            if start < 0:
                break
            start = p.find('https://', start)
            end = p.find('\"', start)
            link = p[start:end]
            page.link.append(link)
            start = end


    for url in linkDict:
        if linkDict[url].link:
            addScore = linkDict[url].baseScore / len(linkDict[url].link)
            for l in linkDict[url].link:
                if l in linkDict:
                    linkDict[l].linkScore += addScore

    items = list(linkDict.items())
    items.sort(key=lambda x: (-(x[1].baseScore + x[1].linkScore), x[1].index))

    answer = items[0][1].index
    return answer

word = "Muzi"
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
print(solution(word, pages))