function solution(board, moves) {
    let basket = []
    let cnt = 0 
    
    for (let m of moves){
        let d = 0
        let flag = true
        while (board[d][m-1] == 0){
            d++
            if (d === board.length){
                flag =false
                break
            }
        }
        if (flag){
            let doll = board[d][m-1]
             board[d][m-1] = 0
            if (basket[basket.length-1] === doll){
                basket.pop()
                cnt += 2
            }else{
                basket.push(doll)
            }
        } 
    }
    return cnt;
}