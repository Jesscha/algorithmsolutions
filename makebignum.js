function solution(number, k) {
    let numberbefore = 0
    while (k > 0) {
        
        let flag = false;        
        for (let i = 0; i < number.length; i ++) {
            if (i === 0){
                numberbefore = number[i]
                continue
            }else{
                if (Number(number[i]) >Number(numberbefore)){
                    number = number.substr(0, i-1) + number.substr(i);
                    numberbefore = number[i]
                    k --;
                    break
                }
                if (i === number.length-1){
                    flag = true
                    break
            }
            numberbefore = number[i]
            }
        }
        if (flag === true){
            break
        }
    }
    if (k !== 0){
        number = number.slice(0, number.length-k)
    }

    return number;
}

console.log(solution("999999999999999999999999999999999999999999999", 3))

// 간단하게 

// 맨처음 수랑 다음 수랑 비교 한다 다음수가 더 클 경우 이전수를 제거하고 다음수만 살린다. 
// 이걸 k 번 반복하고  만약 수의 끝까지 왔는데, k가 남아 있으면, 그만큼 맨 뒤에서 지운다. 



