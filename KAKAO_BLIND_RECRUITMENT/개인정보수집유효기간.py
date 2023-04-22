def trans_date(year, month, day):
    return (year*28*12) + ((month-1)*28) + day
    
def solution(today, terms, privacies):
    answer = []
    validity = {} # 유효기간 dictionary
    date_today = today.split('.') # 0 - 년, 1 - 월, 2 - 일
    caled_today = trans_date(int(date_today[0]), int(date_today[1]), int(date_today[2])) # 변환된 오늘 날짜

    for t in terms: # 유효기간 dictionary에 약관 종류별 유효기간 넣기
        splited_terms = t.split(' ')
        validity[splited_terms[0]] = int(splited_terms[1])
        
    index = 1
    for i in privacies:
        splited_privacies = i.split(' ')
        date_privacies = splited_privacies[0].split('.')

        year = int(date_privacies[0])
        month = int(date_privacies[1])
        day = int(date_privacies[2])
        
        c_date = trans_date(year, month, day) + validity[splited_privacies[1]] * 28 # 가입일자 계산값 + 유효기간

        if c_date <= caled_today: # 계산된 날짜(보관 기간) <= 계산된 오늘 날짜
            answer.append(index) # 파기될 정보
        index += 1
        
    return answer
