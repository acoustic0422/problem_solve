"""
베스트앨범
https://programmers.co.kr/learn/courses/30/lessons/42579
"""

def solution(genres, plays):
    answer = []

    genres_dict = dict()
    play_dict = dict()

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in genres_dict:
            genres_dict[g] = [(p,i)]
        else:
            genres_dict[g].append((p,i))

        if g not in play_dict:
            play_dict[g] = p
        else:
            play_dict[g] += p

    for g in genres_dict:
        genres_dict[g].sort(key=lambda x: (x[0], -x[1]), reverse=True)

    sorted_play = sorted(play_dict.items(), key=lambda x:x[1], reverse=True)

    for g, p in sorted_play:
        answer.append(genres_dict[g][0][1])
        if len(genres_dict[g]) > 1:
            answer.append(genres_dict[g][1][1])

    return answer


# g = ["classic", "pop", "classic", "classic", "pop"]
# p = [500, 600, 150, 800, 2500]

g = ["a", "a", 'a', 'a', 'a']
p = [500, 600, 700, 700, 200]

print(solution(g,p))