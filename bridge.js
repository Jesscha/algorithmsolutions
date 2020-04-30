function solution(bridge_length, weight, truck_weights) {
  let onBridge = [];
  let time = 0;
  while (true) {
    let truck = truck_weights.shift();
        if (
            onBridge.reduce(
              (acc, item) => (item[1] <= bridge_length? (acc += item[0]) : null),
              truck
            ) <= weight
          ) {
              if(truck){
                onBridge.push([truck, 0]);
              }
          } else {
              if (truck){
                truck_weights.unshift(truck);
              }
          }
          time++;
          for (let i = 0; i < onBridge.length; i++) {
            onBridge[i][1]++;
          }
    if (!onBridge.find( item => 
        item[1] <= bridge_length 
    ) && truck_weights.length === 0 ){
        break
    }
    
  }
  return time;
}
console.log(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]));

/*
시뮬레이션을 그대로 하면 되는 문제, 

다리라는 큐에 트럭을 집어 넣으면 된다.

무게 에 따라서 넣을지 말지를 정하면 됨 




*/
