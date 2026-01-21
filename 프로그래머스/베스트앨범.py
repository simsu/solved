
# dict.items() 함수를 알았다.
# !못풀어서 검색한 문제!
def solution(genres, plays):
    # 장르별 플레이 합계
    genre_view = {}
    # 장르별 플레이 인덱스
    genre_index = {}
    answer = []
    
    for i in range(len(plays)):
        if genres[i] in genre_view:
            genre_view[genres[i]] += plays[i]
            genre_index[genres[i]].append((i, plays[i]))
        else:
            genre_view[genres[i]] = plays[i]
            genre_index[genres[i]] = [(i, plays[i])]
    
    for (g, s) in sorted(genre_view.items(), key=lambda x: x[1], reverse=True):
        for (i, v) in sorted(genre_index[g], key=lambda x: x[1], reverse=True)[:2]:
            answer.append(i)
    
    return answer

genres = ["classic", "pop", "classic", "classic", "pop", "pop", "music"]
plays = [500, 600, 150, 800, 2500, 10, 1]
print(solution(genres, plays))
