function solution(genres, plays) {
  genres = genres.map((item) => (item === "pop" ? "pp" : item));
  let genreHash = [];
  for (let i = 0; i < genres.length; i++) {
    if (genreHash[genres[i]]) {
      genreHash[genres[i]][0].push(i);
      genreHash[genres[i]][1] += plays[i];
      genreHash[genres[i]][0] = genreHash[genres[i]][0].sort(
        (a, b) => plays[b] - plays[a]
      );
    } else {
      genreHash[genres[i]] = [[i], plays[i]];
    }
  }
  let ansset = [];
  for (key in genreHash) {
    ansset.push([genreHash[key][1], genreHash[key][0]]);
  }
  ansset = ansset.sort((a,b)=> b[0] - a[0])
  let answer = [];
  for (let i = 0; i < ansset.length; i++) {
      for (let j = 0; j < 2 ; j++) {
          if (ansset[i][1][j] !== undefined){
            answer.push(ansset[i][1][j])
          }
      }
  }
  return answer;
}
console.log(
  solution(
    ["classic", "pop", "classic", "classic", "pop"],
    [500, 600, 150, 800, 2500]
  )
);

/* 장르별로 모으고 정렬하고 앞에서 2개 씩

1. 장르[키값] = [[노래 인덱스], 총합점]

2. 정렬 후 앞에서 2개씩만 정답에 담기




*/
