function solution(numbers) {
    var answer = 0;
    let result = [];
    let last = [];
    const arr = numbers.split('');
   
    for (let i in arr){ // 배열의 수 만큼 반복
        let t_a = search(arr, parseInt(i)+1); // search의 결과 배열을 받음
        result.push(t_a.map(v => parseInt(v.join('')))); // 결과 배열의 값들을 숫자로 변환 후 경우의 수 배열에 삽입
    }
    result.map(s_arr => last.push(...s_arr)) // 각 숫자의 값들이 담긴 배열을 최종 배열에 삽입
    last = new Array(...new Set(last)); // 중복 제거
    
    for (let num of last){ // 최종 배열의 숫자들을 소수인지 검사
        if (isPrime(num)) answer++; // 소수인 경우 answer 증가
    }
    
    return answer;
}

function search(arr, select_count){
    const rt = []; // 결과 배열
    if(select_count === 1) // 선택 할 수가 1인 경우
        return arr.map(v => [v]); // 각 요소들을 하나의 배열로 반환
    
    arr.forEach((v, ind, origin) => { // 현재 원소, 인덱스, 기존 배열
        const rest = [...origin.slice(0,ind), ...origin.slice(ind+1)]; // 현재 인덱스를 제외한 나머지 배열
        const temp = search(rest, select_count-1); // 선택 수-1개 만큼의 조합을 구하도록 한다
        const add_arr = temp.map(va => [v, ...va]); // 현재 원소, 반환 받은 각 배열을 더한 값
        rt.push(...add_arr) // [현재 원소, 각 조합] 경우의 수를 결과 배열에 넣기
    })
    
    return rt
}

function isPrime(num) {
    if(num === 0 || num === 1){ // 0 혹은 1의 경우 소수가 아님
        return false;
    }
    for(let i=2; i*i<=num; i++){ // 루트num 이하
        if(num % i == 0) return false;
    }
    return true;

}
