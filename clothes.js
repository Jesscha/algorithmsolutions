function solution(n, lost, reserve) {
    let clothes  = [];
    for (let i = 0; i<n; i ++){
        clothes.push(1)
    }
    
    for (let j = 0; j<lost.length; j ++){
        clothes[lost[j]-1] --
    }
    
    for (let k = 0; k<reserve.length; k ++){
        clothes[reserve[k]-1] ++
    }
    
    
    for (let l = 0; l<clothes.length; l ++){
        if (clothes[l] === 0){
            if ( l-1 > 0 &&  clothes[l-1] === 2){
                clothes[l-1] --
                clothes[l] ++
            } else if( l+1 < clothes.length&& clothes[l+1] === 2 ){
                 clothes[l+1] --
                clothes[l] ++
            }
        }
    }
    let answer = 0
     for (let m = 0; m<clothes.length; m ++){
         if (clothes[m] >= 1 ){
             answer ++
         }
     }
    
    return answer;
}

// 전체 체육복을 담은 배열을 하나 만든다.
// lost에 있는 놈들을 0으로 만든다. 
// reserve에 있는 놈들을 2로 만든다. 
// 왼쪽부터 하나씩 순회를 돈다. 0 인 경우 양쪽 옆에 여분이 있는지 확인, 있으면 여분의 놈을 1을 줄이고 본인에게 추가한다. 
// 마지막에 배열안에 1의 개수를 센다.