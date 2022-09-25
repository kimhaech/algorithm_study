function solution(participant, completion) {
    var answer = '';
    const part = participant.sort()
    const comp = completion.sort()
    for (let p in part){
        if(part[p] !== completion[p]){
            answer = part[p]   
            break
        }
    }
    return answer;
}
