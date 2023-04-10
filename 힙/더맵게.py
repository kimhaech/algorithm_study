import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        minn = heapq.heappop(scoville)
        sec = heapq.heappop(scoville)
        heapq.heappush(scoville, minn + 2*sec)
        
        answer += 1
#     scoville.sort(reverse=True) # 정렬
    
#     while scoville[-1] < K: # 모든 음식의 맵기가 K이상일 때 까지 반복
#         if len(scoville) == 1 and scoville[0] < K:
#             return -1
#         else:
#             minn = scoville.pop()
#             sec = scoville[-1]
#             scoville[-1] = minn + 2*sec
#             scoville.sort(reverse=True)
#         answer += 1
        
    return answer
