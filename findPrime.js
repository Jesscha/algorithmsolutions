
function solution(numbers) {
    let set = new Set();
    makeNumber(set, '', numbers.split(""))
    return set.size;
}



function isPrime(num){ 
    if (num < 2) return false;
    for (let i = 2; i < Math.sqrt(num); i++) {
        if (num %i === 0){
            return false
        }
    }
    return true
}

function makeNumber (set, cur, nums){
    if (nums.length === 0) return;
    let clone = nums.slice()
    for (let j in nums){
        let numForAdd = clone.pop();
        let numForCheck = Number(cur + numForAdd)
        if (isPrime(numForCheck)){
            set.add(numForCheck)
        }
        makeNumber(set, cur+numForAdd, clone);
        clone.unshift(numForAdd)
    }
}
console.log(solution("011"))