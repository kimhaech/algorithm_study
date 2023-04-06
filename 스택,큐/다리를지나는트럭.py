def solution(bridge_length, weight, truck_weights):
    answer = 0
    done = 0 # 건넌 트럭 수
    left_weight = weight # 현재 수용 가능 무게
    on_bridge = [] # 현재 다리 위의 트럭의 남은 거리
    on_weight = [] # 현재 다리 위의 트럭의 무게
    trucks = len(truck_weights) # 총 트럭 대수
    
    while done != trucks:
        answer += 1
        
        if truck_weights and len(on_bridge) <= bridge_length and left_weight >= truck_weights[0]:
            left_weight -= truck_weights[0] # 수용 무게 빼기
            on_bridge.append(bridge_length) # 가야 할 거리 추가
            on_weight.append(truck_weights.pop(0)) # 현재 트럭의 무게
        
        for i in range(len(on_bridge)): # 길이 1만큼 진행
            on_bridge[i] -= 1
        
        if on_bridge[0] == 0: # 맨 앞의 트럭이 가야할 거리 == 0 -> 다리의 끝
            on_bridge.pop(0)
            left_weight += on_weight.pop(0)
            done += 1

    answer += 1 # 마지막 다리를 건너는 시간
    
    return answer
