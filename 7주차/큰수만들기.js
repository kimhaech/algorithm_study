function solution(number, k) {
    var answer = '';
    number = number.split('').map(a => {return parseInt(a)});
    let res = [];

    for(let num of number){
        while(num > res.slice(-1) && k !== 0 && res.length > 0){
            res.pop();
            k--;
        }
        res.push(num);
    }
    if(k > 0){
        res = res.slice(0,-k)
    }
    // let res = [];
    // let cur_k = k;
    // const f_len = number.length - k;
    
    // while(cur_k > 0){
    //     let temp = number.slice(0,cur_k+1);
    //     let t_max = Math.max(...temp);
    //     let findex = temp.findIndex(e => e === t_max);
    //     res.push(t_max)
    //     if(res.length === f_len)
    //         break
    //     number = number.slice(findex+1)
    //     cur_k -= findex
    // }
    // if(res.length === f_len){
    //     res.map(e => answer+=e)
    // }else{
    //     number.map(e => res.push(e))
    //     res.map(e => answer+=e)    
    // }
    
    answer = res.join('')
    
    return answer;
}
