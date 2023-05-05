def solution(sizes):
    answer = 0
    left = []
    right = []
    
    for size in sizes:
        if size[0] > size[1]:
            left.append(size[1])
            right.append(size[0])
        else:
            left.append(size[0])
            right.append(size[1])
    
    answer = max(left) * max(right)
    
    return answer
