function solution(bridge_length, weight, truck_weights) {
  let answer = 0 
  let bridge_q =[], weight_q = [];
  let bridge_weight = 0

  do{
      for (let i in bridge_q){
          bridge_q[i] --
      }
      if (bridge_q[0] === 0) {
          bridge_q.shift()
          bridge_weight -= weight_q.shift()
      }
      if (bridge_weight + truck_weights[0] <= weight){
          bridge_q.push(bridge_length)
          weight_q.push(truck_weights[0])
          bridge_weight += truck_weights.shift()
      } 
      answer ++ 
  }while(bridge_q.length >0 )  
  return answer;
}


console.log(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]));
