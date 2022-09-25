function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    const trucks = truck_weights.length; // 트럭의 대수
    let left_weight = weight; // 다리가 수용할 수 있는 무게
    let on_bridge = []; // 다리 위의 트럭
    let on_count = []; // 다리 위의 트럭이 가야 할 길이
    let over = 0; // 다 건넌 트럭 수
    
    while(over != trucks){
        // 들어 올 트럭이 남은 중량 이하, 수용 가능한 트럭 수가 남은 경우 - 진입 가능
        if(truck_weights[0] <= left_weight && on_bridge.length <= bridge_length){
            let cur_truck = truck_weights.shift()
            on_bridge.push(cur_truck)
            on_count.push(bridge_length)
            left_weight -= cur_truck
        }
        for(let t in on_count){
            on_count[t]--;
        }
        answer++;
        if(on_count[0] === 0){
            on_count.shift()
            left_weight += on_bridge.shift()
            over++;
        }
    }
    
    answer++;
    
    return answer;
}
