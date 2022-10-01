function solution(nums) {
    var answer = 0;
    
    const setNums = new Set(nums)
    answer = setNums.size < nums.length/2 ? setNums.size : nums.length/2
    return answer;
}
