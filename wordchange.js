const wordDiffCheck = (str1, str2)=> {
    let cnt = 0;
    for(let i in str1){
        if (str1[i] != str2[i] ){
            cnt++
            if (cnt >1){
                return false
            } 
        }
    }
    if (cnt === 1){
        return true
    }
    return false
}



function solution(begin, target, words) {
    if (words.indexOf(target) === -1){
        return 0
    }
    var answer = 0;
    let t = -1
    let q = [begin]
    while (q.length >0 ){
        console.log(q)
        t++
        let len =q.length
        for (let i =0 ; i <len; i++){
            let cur = q.shift()
            if (cur === target ){
                return t
            }
            for (let j of words){
                if (wordDiffCheck(cur, j)){
                    q.push(j)
                }
            }

        }
    }
    return answer;
}

console.log(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))