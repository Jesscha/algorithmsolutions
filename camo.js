//통과는 했지만 더 잘 쓰는 법을 알고 싶음 

function solution(clothes) {
    const hashed = []
    for (let i = 0; i < clothes.length ; i ++){
        hashed[clothes[i][1]] ? (hashed[clothes[i][1]].push(clothes[i][0])) : (hashed[clothes[i][1]]= [clothes[i][0]])       
    }
    let vlen = [] 
    for (let key in hashed){
        vlen.push(hashed[key].length + 1)
    }
    let answer = 1 
    for (let i =0; i < vlen.length; i ++ ){
        answer = answer*vlen[i]
    }    
    return answer -1
}

// 배우고 싶은 코드 

function solution(clothes) {
    return Object.values(clothes.reduce((obj, t)=> {
        obj[t[1]] = obj[t[1]] ? obj[t[1]] + 1 : 1;
        return obj;
    } , {})).reduce((a,b)=> a*(b+1), 1)-1;    
}

