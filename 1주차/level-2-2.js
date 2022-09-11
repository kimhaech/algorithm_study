/*
위치값을 가지는 배열과 중요도 배열의 첫번째 값을 계속 삭제하고 남은 배열의 최대값과 비교한다.
결과에 따라 그대로 삭제 혹은 푸시를 한다.
*/
function solution(priorities, location) {
    var answer = 0;
    let order = []
    
    for(let i = 0; i < priorities.length; i++){
        order.push(i)
    }
    
    while(true){
        let t = priorities.shift()
        let o = order.shift()
        
        if(t >= Math.max(...priorities)){
            answer++;
            if (o === location){
                break;
            }
        }else{
            priorities.push(t)
            order.push(o);
        }
    }
    
    return answer;
}
