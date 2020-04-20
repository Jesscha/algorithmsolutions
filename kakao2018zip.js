

function solution(msg) {
    const alphas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split('')
    console.log(alphas)
    const ans = [] 
    
    while(msg) {
        let temp = '';
        for ( i = 0; i< msg.length; i ++) {
            temp = msg.slice(0, i+1);
            if (alphas.indexOf(temp)=== -1){
                ans.push(alphas.indexOf(temp.slice(0,temp.length-1))+1);
                break
            }
            if (i === msg.length -1 ){
                ans.push(alphas.indexOf(temp.slice(0,temp.length))+1);
            }
        }
        alphas.push(temp);
        console.log(alphas)
        msg = msg.slice(i)
    }
    return ans;
}

console.log(solution("KAKAO"))
