import heapq

def solution(operations):
    answer = []
    count = 0
    aheap = [] # 최소힙
    dheap = [] # 최대힙
    
    for op in operations:
        typ, val = op.split(' ')
        if typ == 'I': # 삽입 연산
            heapq.heappush(aheap, int(val)) # 최소힙 추가
            heapq.heappush(dheap, -int(val)) # 최대힙 추가
            count += 1 # 길이 추가
        else: # 삭제 연산
            if count == 0: # 큐의 길이가 0
                pass
            else: # 큐의 길이가 1이상
                if int(val) > 0: # 최댓값 제거
                    heapq.heappop(dheap)
                    count -= 1
                else: # 최솟값 제거
                    heapq.heappop(aheap)
                    count -= 1
                    
    temp_list = []
    while dheap:
        temp_list.append(-dheap.pop())
        
    intersection = list(set(aheap) & set(temp_list))
    
    if count == 0 or len(intersection) == 0: # 큐가 비었음
        answer = [0,0]
    else:
        answer = [max(intersection), min(intersection)]
        
    return answer
