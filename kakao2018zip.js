

function solution(msg) {
    const alphas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    const ans = [] 
    const visit = []
    for(let i = 0; i < msg.length; i++){
        visit.push(0)
    }
    let txtlen = 1
    let textbefore
    for(let i = 0; i< msg.length; i++){
        if (txtlen !== 1 ){
            txtlen -=1
            continue
        }
        let text = msg[i]
        let ii = i 
        while (alphas.includes(text)){
            ii += 1 
            textbefore = text
            text += msg[ii]
        }
        ans.push(alphas.indexOf(textbefore)+1)
        alphas.push(text)
        txtlen = textbefore.length
    }
    return ans;
}

console.log(solution("KAKAO"))

/*
풀이 방법 

인덱스 배열과 값 배열을 만든다.

언제까지 글자수를 체크해야 할지 모르겠다. 
비짓을 만들면 해결 할 수 있다. 해당 글자가 비짓 되었으면 패스를 하자 


*/

