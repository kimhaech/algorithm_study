def solution(numbers):
    answer = ''

    numbers = list(map(str, numbers)) # 문자열로 변환
    numbers.sort(reverse=True, key=lambda x: x*4)
    # mySort(numbers) # 정렬 함수 - 효율성 문제

    answer = "".join(numbers)
    if int(answer) == 0:
        answer = "0"
        
    return answer

# def mySort(numbers): # 효율성 문제
#     for i in range(len(numbers)-1): # 기준 원소
#         for j in range(i+1, len(numbers)): # 비교 원소
#             # 합쳐서 더 큰 수를 만들어내는 경우로 정렬
#             if numbers[j] + numbers[i] > numbers[i] + numbers[j]:
#                 numbers[i], numbers[j] = numbers[j], numbers[i] 
