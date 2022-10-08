function solution(answers) {
    var answer = [];
    const pattern = {'1': [1,2,3,4,5], '2': [2,1,2,3,2,4,2,5],'3':[3,3,1,1,2,2,4,4,5,5]}; // 각 패턴
    
    const len1 = pattern['1'].length; // 1번 패턴 길이
    const len2 = pattern['2'].length; // 2번 패턴 길이
    const len3 = pattern['3'].length; // 3번 패턴 길이
    
    let count = [0,0,0] // 각 패턴별 정답 수
    
    for(let ind in answers){ // 정답 확인
        let ans = answers[ind];
        if(pattern['1'][ind%len1] === ans) count[0]++;
        if(pattern['2'][ind%len2] === ans) count[1]++;
        if(pattern['3'][ind%len3] === ans) count[2]++;
    }
    const maxValue = Math.max(...count) // 최고 득점 수
    count.map((value,index) => {
        if(value === maxValue)
            return answer.push(index+1);
    })
    answer.sort() // 정렬
    return answer;
}
