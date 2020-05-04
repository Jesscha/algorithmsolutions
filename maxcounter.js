function solution(N, A) {
    let counters =new Array(N).fill(0)
    for (let num of A){
        
        if (num === N+1){
            let maxNum = Math.max(...counters)
            counters.fill(maxNum)
        }
        else{
            counters[num-1] ++;
        }
    }
    return counters
}