def solution(priorities, location):
    answer = 0
    index = []
    
    for i in range(len(priorities)): # save index
        index.append(i)
    
    count = 1
    while priorities:
        if priorities[0] == max(priorities): # max value case
            priorities.pop(0)
            if index.pop(0) == location: # index == location
                answer = count
                break
            else: 
                count += 1
        else:
            priorities.append(priorities.pop(0))
            index.append(index.pop(0))
            
        
    return answer
