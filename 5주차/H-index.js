function solution(citations) {
    var answer = 0;
    let count = 0; // h 카운트
    let temp;
    
    citations.sort((a,b)=>{return b-a}); // 내림차순 정렬

    for(let i in citations){
        count++;
        if(count <= citations[i]){
            temp = count;
        }else{ // count > citations[i]
            break;
        }
    }
    answer = temp; // 마지막으로 카운트 한 수
    
    if(!citations[0]) answer = 0 // all value 0 case
    
    return answer;
}
