function solution(n, costs) {
    let answer = 0,
    island = [],
    bridge = [],
    total =0
    
    costs.sort((a,b)=>a[2]-b[2])

    island[costs[0][0]] =true;
    island[costs[0][1]] =true;
    bridge[0] = true;
    answer += costs[0][2]
    total += 1

    while (total < n-1){
        for (let i = 1; i< costs.length; i ++){
            let [start, end, cost] = cost[i]
            if (
                !bride[i] && 
                (
                    (island[start] && !island[end] ) ||
                    (island[end] && !island[start])
                )
            ){
                island[start] =true;
                island[end] = true;
                bridge[i] = true; 
                answer += cost;
                total ++ 
                break 
            }
        }
    }

    return answer



}




console.log(
  solution(4, [
    [0, 1, 1],
    [0, 2, 2],
    [1, 2, 5],
    [1, 3, 1],
    [2, 3, 8],
  ])
);
