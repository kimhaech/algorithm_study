/*
첫날을 기준으로 비교 시작
기준 날보다 다음날의 작업에 소요되는 시간이 더 적거나 같은 경우 완료될 작업에 추가
ex) 10 7 8 6 11
10일 기준 7일 통과, 8일 통과, 6일 통과 후 11일에서 걸러진다.
return [4,1]
하루 전날을 기준으로 한다면 10 7 까지만 추가되고 7과 8을 비교하면 8이 더 크기에 추가가 되지 않는다.
시작하는 날짜를 최대 기준일로 두고 검사한다.
*/
function solution(progresses, speeds) {
    var answer = [];
    let sum = 1;
    let left = [];
    let temp = 0;
    
    for(let i in progresses){
        temp = Math.ceil((100 - progresses[i])/speeds[i])
        left.push(temp)
    }
    
    let temp_biggest = left[0]
    
    for(let i = 1; i < left.length; i ++){
        if (temp_biggest >= left[i]){
            sum += 1
        }else{
            answer.push(sum)
            sum = 1
            temp_biggest = left[i]
        }
    }
    
    answer.push(sum) // 남은 sum 추가
    
    return answer;
}
