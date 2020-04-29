function solution(participant, completion) {
   let ret = [] 
   let hased = [] 
   participant.forEach(entry => {
       hased[entry] = hased[entry] ? hased[entry] + 1 : 1
   })
   completion.forEach(entry => {
       hased[entry] = hased[entry] -1 
   })

   for (let key in hased) {
       if (hased[key] >= 1 ) return key
   }


}

console.log(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
