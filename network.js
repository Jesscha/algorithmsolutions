function solution(n, computers) {
    let answer = 0
    let visit = "0".repeat(n).split("")
    for (let i = 0; i <n; i++) {
        if (visit[i] === "0"){
            answer ++; 
            let q = [i];
            while(q.length >0){
                let cur = q.shift();
                visit[cur] = 1 
                for (let j = 0; j < computers[cur].length; j++) {
                    if(visit[j]==="0" && computers[cur][j]=== 1){
                        q.push(j)
                    }   
                }
            }
        }
        
    }
    return answer;
}

console.log(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))