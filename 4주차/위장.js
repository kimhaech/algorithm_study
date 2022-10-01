function solution(clothes) {
    var answer = 0;    
    let clothesMap = new Map();
    
    for (let cloth of clothes){
        let tempArray = clothesMap.get(cloth[1]); // 종류
        if(tempArray){ // 옷의 종류에 해당하는 의상이 있는 경우
            tempArray.push(cloth[0]);
            clothesMap.set(cloth[1],tempArray);    
        }else{ // 옷의 종류에 해당하는 의상이 없는 경우
            clothesMap.set(cloth[1],[cloth[0]]);
        }
    }

    let temp = 1; // 연산을 위한 변수
    for (let cloth of clothesMap.keys()){
        temp *= clothesMap.get(cloth).length + 1; // 옷의 수 + 1
    }
    answer = temp - 1;
    
    return answer;
}
