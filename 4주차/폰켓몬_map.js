function solution(nums) {
    var answer = 0;
    let map = new Map();
    
    for(let p of nums){
        map.set(p, map.get(p) > 0 ? map.get(p)+1 : 1)
    }
    answer = map.size < nums.length/2 ? map.size : nums.length/2
    return answer;
}
