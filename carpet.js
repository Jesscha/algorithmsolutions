function solution(brown, red) {
    for (let i = 0 ; i < red; i ++) {
        for (let j = 0; j<= i; j++){
            let redNeeded = (i+1) * (j+1);
            if (redNeeded === red){
                if(brown ===((i+1)+2)*2 + (j+1)*2 ){
                    return [i+1+2, j+1+2]
                }
            }
        } 
    }   
}

console.log(solution(10, 2))

