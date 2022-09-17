function solution(array, commands) {
    var answer = [];
    
    for(let i of commands){
        let result = array.slice(i[0]-1, i[1]);
        if(result.length !== 1) result.sort((a,b) => {return a-b});
        answer.push(result[i[2]-1]);
    }
    
    return answer;
}
