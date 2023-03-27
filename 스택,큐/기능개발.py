import math

def solution(progresses, speeds):
    answer = []
    div = []
    for i in range(len(progresses)):
        temp = int(math.ceil((100 - progresses[i])/speeds[i]))
        div.append(temp)
    
    count = 1
    cur = div[0]
    for i in range(1,len(div)):
        if cur >= div[i]: # 앞의 남은 작업 일 수가 다음의 작업 일 수 보다 크거나 같은 경우
            count += 1 # 작업 완료 수 증가
        else: # 앞의 남은 작업 일 수 보다 다음의 작업 일 수가 큰 경우
            answer.append(count)
            count = 1 # 카운트 초기화
            cur = div[i] # 다음의 작업을 다시 기준으로 설정
    
    answer.append(count) # 추가하지 못한 마지막 작업의 합을 추가
    
    return answer
