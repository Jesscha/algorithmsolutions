function solution(numbers, target) {


    function combinations(n, r) 
{
  if (n===r) 
  {
    return 1;
  } 
  else 
  {
    r=(r < n-r) ? n-r : r;
    return product_Range(r+1, n)/product_Range(1,n-r);
  }
}

    var answer = 0;
    return answer;
}