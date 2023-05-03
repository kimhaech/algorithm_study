def solution(genres, plays):
    answer = []
    total_play = {} # 장르별 재생 횟수 총합
    genres_play = {} # 장르별 고유번호와 재생 수
    
    for i in range(len(genres)): # 장르별 dictionary 값 넣기
        if genres[i] in total_play.keys():
            total_play[genres[i]] += plays[i]
            genres_play[genres[i]].append([plays[i],i])
        else:
            total_play[genres[i]] = plays[i]
            genres_play[genres[i]] = [[plays[i],i]]
    
    # 장르별 재생 수 합 내림차순 정렬
    desc_total_play = list(total_play.items())
    desc_total_play.sort(key=lambda x : -x[1])
    
    for key, value in genres_play.items(): # 장르별 재생 수 내림차순 정렬
        value.sort(key=lambda x : -x[0])
        genres_play[key] = value    
    
    for val in desc_total_play:
        key = val[0]
        if len(genres_play[key]) >= 2: # 2개이상의 값을 가지는 경우
            val_list = genres_play[key][:2]
            answer.append(val_list[0][1])
            answer.append(val_list[1][1])
        else:
            answer.append(genres_play[key][0][1])

    return answer
