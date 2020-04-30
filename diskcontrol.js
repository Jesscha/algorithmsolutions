function solution(jobs) {
    let len  = jobs.length
    let answer = 0, time = 0, cur ;  
    jobs.sort((a,b) => a[1]-b[1])
    
    while (jobs.length > 0){
        let flag = true 
        for (let i in jobs) {
            if (jobs[i][0] <= time){
                cur = jobs[i]
                time += jobs[i][1]
                answer += time - jobs[i][0]
                flag = false 
                jobs.splice(i,1)
                break
            }
        }
        if (flag === true) time ++
    }
    answer = Math.floor(answer/len)
    return answer
}

console.log(solution([[0, 3], [1, 9], [2, 6]]))