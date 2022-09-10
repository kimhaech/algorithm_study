function solution(arr)
{
    var answer = [];
    
    answer.push(arr[0])
    
    for (let i = 1; i < arr.length; i++) {
        if(answer.slice(-1)[0] !== arr[i]){
            answer.push(arr[i])
        }
    }
    
    return answer;
}
