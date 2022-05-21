"""
매칭 점수
https://programmers.co.kr/learn/courses/30/lessons/42893?language=python3
"""


class web_page(object):
    def __init__(self):
        self.index = -1
        self.base_score = 0
        self.link_score = 0
        self.link = []


def solution(word, pages):
    NOTATION = 'abcdefghijklmnopqrstuvwxyz'
    word = word.lower()
    answer = 0

    web_pages = dict()

    for i in range(len(pages)):
        p = pages[i]
        head_s = p.find('<head>')
        head_s = p.find('<meta property="og:url" content=', head_s)
        head_s = p.find('https://', head_s)
        url = ''
        while p[head_s] != '"':
            url += p[head_s]
            head_s += 1
        temp_page = web_page()
        temp_page.index = i

        body_s = p.find('<body>', head_s)
        body_e = p.find('</body>', body_s)

        while body_s < body_e:
            temp_url = ''
            body_s = p.find('<a href=', body_s)
            if body_s == -1:
                break
            body_s = p.find('https://', body_s)
            while p[body_s] != '"':
                temp_url += p[body_s]
                body_s += 1
            temp_page.link.append(temp_url)

        low_p = p.lower()
        cnt = 0
        temp = ''
        for c in low_p:
            if c in NOTATION:
                temp += c
            else:
                if temp == word:
                    cnt += 1
                temp = ''
        if temp != '':
            if temp == word:
                cnt += 1

        temp_page.base_score = cnt
        web_pages[url] = temp_page

    for url in web_pages:
        num_link = len(web_pages[url].link)
        if num_link == 0:
            continue
        else:
            add_score = web_pages[url].base_score / num_link

            for li in web_pages[url].link:
                if li in web_pages:
                    web_pages[li].link_score += add_score

    max_score = -1
    for url in web_pages:
        total_score = web_pages[url].base_score + web_pages[url].link_score
        if total_score > max_score:
            max_score = total_score
            answer = web_pages[url].index

    return answer


word = 'Muzi'
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]

print(solution(word, pages))
