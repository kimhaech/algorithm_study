function solution(people, limit) {
    var answer = 0;
    
    people = people.sort((a,b) => {return a-b});
    
    while(people.length !== 0){ // people 배열이 존재하는 동안 반복
        let temp = limit - people.pop();
        while(people[0] <= temp) {
            temp -= people.shift();           
        }
        answer++;
    }
    
    return answer;
}
