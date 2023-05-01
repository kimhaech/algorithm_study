def solution(nums):
    answer = 0
    len_nums = len(nums)/2
    set_nums = set(nums)

    if len(set_nums) > len_nums:
        answer = len_nums
    else:
        answer = len(set_nums)
        
    return answer
