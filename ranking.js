function solution(n, results) {

    // 각 선수의 이기고 진 사람을 기록할 set을 담을 array를 만든다. 
    let arrWin = [] 
    for (let i = 0; i < n+1; i++) {
        const wins = new Set()
        arrWin.push(wins)
    }

    let arrLose = [] 
    for (let j = 0; j < n+1; j++) {
        const wins = new Set()
        arrLose.push(wins)
    }
    for (let index = 1; index <n+1; index++){
        for (let re of results){
            
            let [winner, loser] = re
            // 승부 자체를 기록
            if (winner === index){
                arrWin[index].add(loser);
            }
            if (loser === index){
                arrLose[index].add(winner);
            }
            // 다른 승부를 이식
            for (let a of arrLose[index]){
                for (let aa of arrWin[index] ){
                    arrWin[a].add(aa)
                }
            }
            for (let b of arrWin[index]){
                for (let bb of arrLose[index] ){
                    arrLose[b].add(bb)
                }
            }    
        }


    }
   
    let answer = 0;  
    for (let k in arrWin){
        if (arrWin[k].size + arrLose[k].size ===n-1){
            answer++
        }
    }  

  return answer;
}

console.log(
  solution(8, [[1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8], [4, 5]])
);

// 승패의 개수가 n-1개 들어 있는 사람의 순위는 정확하게 파악할 수 있다.

// 이를 위한 구현 방법

// 각 번호 별로 이긴 set과 진 set을 만든다.

// for 문을 돌린다. 각 항의 0번째가 1번째를 이기는 것이므로 이를 각기 기록한다.

// 문제는 직접 승부가 아니라 다른 이들과의 승부로 결정되는 것을 기록하는방법

// 누군가에게 졌다면, 그 사람이 이긴 모든 사람은 나를 이긴다.

// 누군가를 이겼다면 그 사람이 진 모든 사람은 나에게 진다.

// 위의 두가지를 기본 원리로 삼아 알고리즘을 짠다.

// 다시 정리하면,
// 1. 이긴 진 자체를 기록
// 2. 이긴 사람의 진 리스트를 진 사람의 진 리스트에 추가
// 3. 진 사람의 이긴 리스트릴 이긴 사람의 이긴 리스트에 추가
// 4. 각 선수의 정보가 업데이트 될 때마다 추가로 갱신 
// 5. 이긴 진 리스트 합처서 개수가 n-1개 이면 count


// 3try 만에 배운 것, 순서가 중요하다. 마지막에 앞의 전적을 업데이트 하는 일이 발생하면 그것과 관련된 다른 승부를 업데이트 할 수 없었다. 

// 4try 적용점. 순서로 깔짝깔짝 고치지 말고 처음부터 완전히 승부를 기록하면 된다.