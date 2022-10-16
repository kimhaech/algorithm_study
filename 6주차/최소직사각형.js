// 명함 각 길이를 정렬하면서 가로, 세로 최대값을 갱신 -> 최대 최소를 곱한 값이 모든 명함의 길이를 수용하는 지갑의 사이즈가 된다.
function solution(sizes) {
    var answer = 0;
    let lm = 0;
    let rm = 0;
    
    for(let card of sizes){
        card.sort((a,b) => {return a-b});
        lm = card[0] > lm ? card[0] : lm;
        rm = card[1] > rm ? card[1] : rm;
    }
    
    return answer = lm*rm;
}
