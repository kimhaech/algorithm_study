def solution(citations):
    answer = 0
    count = 0 # 인용횟수를 체크한 논문 수
    citations.sort(reverse=True) # 내림차순 정렬
    
    if citations[0] == 0: # 첫 값이 0 인경우 0 반환
        return 0
    
    for h in citations:
        count += 1 # 논문 카운트 증가
        if count == h: # 현재 체크한 논문 수와 인용 수가 같은 경우
            answer = h
            break
        elif count > h: # 현재 체크한 논문수가 인용 수 보다 큰 경우
            answer = count-1
            break

    if answer == 0 and count > 0: # 모든 논문을 다 체크한 경우 카운트한 논문 수로 반환
        answer = count   
        
    return answer
