function solution(numbers) {
    var answer = 0;
    var set = new Set();
    makeNumbers(set , '' , numbers.split(''));
    return set.size;
}

function issosu(num) {
    if( num < 2) return false;
    for (var i =2; i <= num / 2 ; i++) {
        if( num % i === 0) return false;
    }
    return true;
}

function makeNumbers(set , cur, nums) {
    if( nums.length === 0 ) return;
    var clone = nums.slice().reverse();
    nums.forEach(function(i) {
        var su = clone.pop();
        var num = Number(cur+su);
        if ( issosu(num)) {
            set.add(num);
        }
        makeNumbers(set, cur+su , clone);
        clone.unshift(su);
    }) 
}