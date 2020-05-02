function solution(N, number) {
  var answer = 0;
  let first = new Set();
  first.add(N);
  let dp = [0];
  dp.push(first);
  let k = 1;
  while (k < 9) {
    k++;
    const SetToAdd = new Set();
    SetToAdd.add('1'.repeat(k)*N);
    // console.log(dp[0][0])
    for (let i = 1; i <= k / 2; i++) {
      // dp[i]에 대하여 dp[k-i]의 모든 원소를 사칙연산 하는 알고리즘
      for (let j of dp[i]) {
        for (let l of dp[k - i]) {
          SetToAdd.add(j + l);
          SetToAdd.add(j - l);
          SetToAdd.add(l - j);
          SetToAdd.add(j * l);
          if (l !== 0) {
            SetToAdd.add(parseInt(j / l));
          }
          if (j !== 0) {
            SetToAdd.add(parseInt(l / j));
          }
        }
      }
      // dp[i]의 원소에 대하여  dp[k-i]의 모든 원소를 사칙연산 한 값을 세트에 넣고 이를 dp[k]로 두는 알고리즘
    }

    dp.push(SetToAdd);
    if (SetToAdd.has(number)) {
      return k;
    }
  }
  return -1;
}

console.log(solution(5, 12));
