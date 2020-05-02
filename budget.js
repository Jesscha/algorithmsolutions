function solution(budgets, M) {
    
    let right = Math.max(...budgets);
    let answer;
    let left = 0;
    let mid;
    while ( right >= left ){
        
        mid =  parseInt((right+left)/2);
        console.log({left, right, mid})
        let total = 0;
        for ( let budget of budgets ){
            if(budget > mid){
                total += mid;
            }else{
                total += budget;
            }
        }
        if (total > M){
            right = mid-1
        }else if(total<M) {
            if (total >0){
                answer = mid
                console.log({answer}) //M보다 작은 것중 최대니까
            }
            left = mid +1
        }else{
            return mid
        }
    }
    return answer
}

console.log(solution([120, 110, 140, 150], 485))