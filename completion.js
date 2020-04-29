function solution(participant, completion) {
    let answer = []
    for (let i = 0; i < participant.length; i++) {
        if ( completion.includes(participant[i]) === false){
            return participant
        }else{
            const idx = completion.indexOf(participant[i])
            completion.splice(idx, 1)
        }
    }
    return answer[0];
}

console.log(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
