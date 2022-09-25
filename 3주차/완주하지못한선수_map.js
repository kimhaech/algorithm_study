function solution(participant, completion) {
    var answer = '';
    const comp = new Map()
    for (let c of completion){
        comp.set(c, comp.get(c) === undefined ? 1 : comp.get(c)+1)
    }
    
    participant.map(part => {
        comp.get(part) > 0 ? comp.set(part,comp.get(part)-1) : answer = part
    })
    return answer;
}
