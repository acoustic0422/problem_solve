"""
가사 검색
https://programmers.co.kr/learn/courses/30/lessons/60060
"""

class Node(object):
    def __init__(self):
        self.count = 0
        self.child = dict()

class Trie(object):
    def __init__(self):
        self.root = Node()

    def search(self,word):
        curr = self.root
        for c in word:
            if c == '?':
                return curr.count
            else:
                if c in curr.child:
                    curr = curr.child[c]
                else:
                    return 0
        return curr.count

    def insert(self, word):
        curr = self.root
        curr.count += 1
        for c in word:
            if c not in curr.child:
                curr.child[c] = Node()
            curr = curr.child[c]
            curr.count += 1


def solution(words, queries):
    answer = []

    trie_arr = [0 for _ in range(10001)]
    rev_trie = [0 for _ in range(10001)]

    for w in words:
        l = len(w)
        if trie_arr[l] == 0:
            trie_arr[l] = Trie()
        trie_arr[l].insert(w)
        rw = w[::-1]
        if rev_trie[l] == 0:
            rev_trie[l] = Trie()
        rev_trie[l].insert(rw)

    for q in queries:
        l = len(q)
        if q[0] == '?':
            rq = q[::-1]
            if rev_trie[l] == 0:
                answer.append(0)
            else:
                answer.append(rev_trie[l].search(rq))
        else:
            if trie_arr[l] == 0:
                answer.append(0)
            else:
                answer.append(trie_arr[l].search(q))


    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))

