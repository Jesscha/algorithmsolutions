function solution(routes) {
    routes = routes.sort((a,b)=>(a[1]- b[1]))
    let camPosition = -999999999;
    let camNumber = 0;

    for (let i = 0; i<routes.length; i++ ){
        let [st, ed]  = routes[i]
        if ( st <= camPosition ){
            continue
        }else{
            camPosition = ed 
            camNumber ++
        }
    }
    return camNumber;
}

console.log(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))

