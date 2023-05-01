def solution(clothes):
    answer = 0
    clothes_dict = {}
    clothes_count = []
    
    for cloth in clothes:
        if cloth[1] in clothes_dict.keys():
            clothes_dict[cloth[1]] += 1    
        else:
            clothes_dict[cloth[1]] = 1
    
    for key, value in clothes_dict.items():
        clothes_count.append(value)

    answer = 1
    for i in clothes_count:
        answer *= (i+1)
        
    answer -= 1
    
    return answer
