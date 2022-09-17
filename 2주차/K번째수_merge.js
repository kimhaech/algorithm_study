function solution(array, commands) {
    var answer = [];
    
    for(let i of commands){
        let result = array.slice(i[0]-1, i[1]);
        result = mergeSort(result);
        answer.push(result[i[2]-1]);
    }
    
    return answer;
}

function merge(left, right) {
    let result = [];
    
    while(left.length !== 0 && right.length !== 0){
        left[0] < right[0] ? result.push(left.shift()) : result.push(right.shift());
    }
    
    return [...result, ...left, ...right];
}

function mergeSort(arr) {
    if (arr.length === 1){
        return arr;   
    }
    
    let m = arr.length/2;
    let left = arr.slice(0,m);
    let right = arr.slice(m);

    return merge(mergeSort(left), mergeSort(right));
}
