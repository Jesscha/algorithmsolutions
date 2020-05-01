function solution(baseball) {
  let numlist= '123456789'.split("")
  let set = new Set()

  function checker(num){
      for (let i in baseball){
          let [n, s, b ] = baseball[i]
          let sCompare = 0;
          let bCompare = 0;
          n = String(n)
          
          for (let j in num){
              if (num[j] === n[j]){ 
                sCompare++;
              }
              if (num.indexOf(n[j]) !== -1 ){
                bCompare++;
              }
          }
          bCompare -= sCompare;
          if (sCompare !== s || bCompare !== b){
              return false 
          }
      }
      return true
  }
  
  function makeNumbers(set, cur, numbers){
      if (cur.length === 3){
          if (checker(cur)) {
              set.add(cur);
          }
          return ;
      }
      let clone = numbers.slice();
      for (i in numbers){
        let addnumber = clone.pop();
        let newnum = cur+ addnumber;
        makeNumbers(set, newnum, clone);
        clone.unshift(addnumber)
    }
  }
  
  makeNumbers(set, '', numlist)
  return set.size
}

console.log(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))

// 123 부터 987 까지 모든 수를 주어진 조건에 맞게 흘려 보낸다.

// 마지막까지 살아남은 숫자의 수를 센다.
