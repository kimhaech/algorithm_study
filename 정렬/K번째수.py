def solution(array, commands):
    answer = []
    
    for info in commands: # commands 조회
        temp = array[info[0]-1:info[1]] # slicing
        temp.sort() 
        answer.append(temp[info[2]-1])
    
    return answer
