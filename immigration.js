function solution(n, times) {
    let right = Math.max(...times)*n
    let left = 0
    let answer  = right
    let mid
    while (right >= left){
        mid = parseInt((right+left)/2);
        let total = 0
        for (let inspector of times){
            total += parseInt(mid/inspector);
        }
        if (total >= n){
            answer =mid
            right = mid -1;
        }else if  (total < n){
            left = mid +1;
        }
    }
    return answer 
}

console.log(solution(6, [7, 10]))