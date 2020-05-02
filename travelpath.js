function solution(tickets) {
    let answer =[];
    let destinations = {}
    for (let j of tickets){
        let [from, to]  = j 
        if (destinations[from]){
             destinations[from].push(to) 
             destinations[from].sort()
        } else{
            destinations[from] = [to]
        }
    }
    
    const dfs = (cur, path, destinations)=>{
        if( path.length === tickets.length+ 1 ) {
                answer.push(path)
            return 
        }
        console.log({cur, destinations})
        if (destinations[cur]){
            for (let i of destinations[cur]){
                let tmpDest = JSON.parse(JSON.stringify(destinations))
                tmpDest[cur].splice(tmpDest[cur].indexOf(i), 1)
                let tmpPath = path.slice()
                tmpPath.push(i)
                dfs(i, tmpPath, tmpDest)
            }
        }
    }
    dfs("ICN", ["ICN"], destinations)
    
    return answer.sort()[0];
}


console.log(solution([["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]))