function solution(numbers) {
    var answer = '';
    const snum = sort(numbers.map(num => num.toString()))
    
    answer = snum.join('')
    
    const zero_case = parseInt(answer) // 0의 경우
    if(zero_case === 0)
        return "0";
    
    return answer;
}

function sort(arr) {
    return arr.sort(function(a,b) {
        return a+b > b+a ? -1 : 1;
    })
}
