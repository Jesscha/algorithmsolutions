function solution(progresses, speeds) {
    var answer = [];
    let dayUntileDone = []
    let  cnt = 0
    
    for (let i in progresses){
        dayUntileDone.push(Math.ceil((100 - progresses[i])/speeds[i]))
    }

    let dayBefore = dayUntileDone[0]

    let j = 0
    do{ 
        if (dayUntileDone[j] > dayBefore){            
            dayBefore = dayUntileDone[j]
            answer.push(cnt)
            cnt = 0
        }
        if (dayUntileDone[j] <= dayBefore){
            cnt ++
        }
        if (j === dayUntileDone.length -1) {
            answer.push(cnt)
        }
        j ++ 
    }
    while( j < dayUntileDone.length)


    return answer
    }
    
console.log(solution([93, 30, 55], [1, 30, 5]))


