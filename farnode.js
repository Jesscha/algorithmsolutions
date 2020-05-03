function solution(n, edge) {
  let nodeMap = [];
  for (let i = 0; i < n + 1; i++) {
    let tmp = [];
    for (let j = 0; j < n + 1; j++) {
      tmp.push(0);
    }
    nodeMap.push(tmp);
  }
  for (let i in edge) {
    let [fr, to] = edge[i];
    nodeMap[fr][to] = 1;
    nodeMap[to][fr] = 1;
  }
  let visit = "0".repeat(n + 1).split("");
  let cnt = 0;
  let q = [1];
  visit[1] = cnt;
  while (q.length > 0) {
    cnt++;
    let len = q.length
    for (let j =0; j <len; j++) {
      let cur = q.shift();
      for (let i in nodeMap[cur]) {
        if (visit[i] === "0" && nodeMap[cur][i] === 1) {
          q.push(i);
          visit[i] = cnt;
        }
      }
    }
  }
  visit.splice(0,1)
  let maxlen = Math.max(...visit)
  var answer = 0;
  return visit.filter(item=> item === maxlen).length
}

console.log(
  solution(6, [
    [3, 6],
    [4, 3],
    [3, 2],
    [1, 3],
    [1, 2],
    [2, 4],
    [5, 2],
  ])
);

// 전략 각 노드까지의 위치를 계산한다
