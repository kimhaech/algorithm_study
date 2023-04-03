def solution(prices):
    answer = []
    
# 풀이 1
#     for i in range(len(prices)):
#         count = 0
#         for j in range(i+1,len(prices)):
#             if prices[i] <= prices[j]:
#                 count += 1
#             else:
#                 count += 1
#                 break
#         answer.append(count)
        
# 풀이 2
    stack = []
    
    stack.append(prices.pop()) # 가장 끝 원소
    answer.append(0) # 무조건 0
    
    for i in range(len(prices)-1, -1, -1):
        count = 0 # 카운트 초기값

        for j in range(len(stack)-1, -1, -1):
            count += 1 # 1초 -> 카운트 +1
            if prices[i] > stack[j]: # prices의 현재 값이 stack에 있는 값보다 큰 경우 -> 감소
                break
        answer.append(count)
        stack.append(prices[i])
        
    answer.reverse()
    
    return answer
