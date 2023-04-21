import heapq

def solution(jobs):
    answer = 0
    heap = []
    jobs.sort(key=lambda x: x[0])
    time_list = []
    endtime = 0
    
    while len(jobs) > 0:  # 남은 작업이 없을때 까지 반복
        while jobs:
            temp = jobs[0]
            if temp[0] <= endtime:  # 현재 시간 이전에 도착한 작업이 있는 경우
                jobs.pop(0)
                heapq.heappush(heap, (temp[1], temp))
            else:
                break
                
        if len(heap):  # 대기한 작업이 있는 경우 or 딱 맞게 시작
            cur_task = heapq.heappop(heap)  # 우선순위가 높은 작업 pop
            time = (endtime - cur_task[1][0]) + cur_task[1][1]  # 대기시간 + 소요시간
            time_list.append(time)
            endtime += cur_task[1][1]  # endtime(현재 시간) 설정
        else:
            endtime+=1
            
        while heap:
            jobs.append(heapq.heappop(heap)[1])
        jobs.sort(key = lambda x : x[0])
        
    answer = sum(time_list)//len(time_list)

    return answer
