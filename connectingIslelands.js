function solution(n, costs) {
    let answer = 0,
      island = [],
      bridge = [],
      total = 0;
    costs.sort((a, b) => a[2] - b[2]); // 비용이 낮은 거 순으로 정렬
    island[costs[0][0]] = true; // cost에 제일 앞에 있는 섬 방문 처리 
    island[costs[0][1]] = true; // 
    bridge[0] = true; // 건설된 다리 하나 지어졋다고 친다.  다리 번호 == costs 번호
    answer += costs[0][2]; // 지어진 비용 추가
    total += 1; // 지어진 다리 개수 증가
  
    while (total < n - 1) { // 지어진 다리 개수가 섬개수 -1개 일때, 즉 다리를 다 지었을 때 종료
      for (let i = 1; i < costs.length; i++) { 
        let [start, end, cost] = costs[i]; // 각 코스트별 디스트럭쳐링 
        if (
          !bridge[i] && 
          ((island[start] && !island[end]) || (island[end] && !island[start])) //둘 중 하나만 방문 한 경우 
        ) {
          // 그 다리를 사용한다.
          island[start] = true; 
          island[end] = true;
          bridge[i] = true;
          answer += cost;
          total++;
          break;
        }
      }
    }
  
    return answer;
  }
  
  
  // 설명해 보자 
  
  // 비용이 낮은 거 순으로 정렬한다.
  // 제일 비용이 낮은 다리는 무조거 쓸 테니까  비용이 낮은 다리를 일단 하나 건설 한다. 
  // 다리별 비짓 처리를 해 준다. 
  // while 문을 돌린다. 지을 수 있는 다리의 조건은 그 다리를 지은적 없고 두 섬중에 하나는 연결되어 있는 것 
  // 다리를 하나 지으면 for 문을 break 한다.
  // 그러면 다시 while 문에 의해서 for 문이 돌아간다. 필요한 다리 개수가 다 차면 while 문이 종료된다. 