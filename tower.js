function solution(heights) {
    return heights.map((i, v) => {
        console.log(v,i)
        while (i) {
            i--;
            if (heights[i] > v) {
                return i + 1;
            }
        }
        return 0;
    });
}

console.log(solution([1, 5, 3, 6, 7, 6, 5]))