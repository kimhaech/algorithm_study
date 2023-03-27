def solution(arr):
    answer = []
#     answer.append(arr.pop(0)) # 맨 앞 요소 빼기
    
#     while len(arr) > 0: 
#         if answer[-1] != arr[0]: # stack안의 원소와 현재 원소가 다른 경우
#             answer.append(arr.pop(0))
#         else:
#             arr.pop(0)
    answer.append(arr[0]) # 맨 앞 요소 넣기
    for i in range(1, len(arr)): # 맨 앞 요소 제외~ 마지막 원소까지 반복
        if answer[-1] != arr[i]: # 현재의 요소와 이전의 요소가 다른 경우(연속 X)
            answer.append(arr[i]) # 추가
        
    return answer
