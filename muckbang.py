def solution(food_times, k):
    sumfood = sum(food_times)
    if k >= sumfood:
        return -1
    lastFood = 0
    i = 0
    while k >= 0:
        i %= len(food_times)
        if food_times[i] != 0:
            food_times[i] -= 1
            lastFood = i+1
            k -= 1
        i += 1


    return lastFood
print(solution(	[0, 0, 2, 4, 5, 6], 1))

'''
1. 0이 발견되는 경우 다음 숫자까지 바로 건너 뛸 수 있도록 dict를 마련한다. 
2. 처음부터 순회를 돌면서 k를 깎아 나간다. 
    0이 발견되면 1에서 준비한 dict를 통해서바로 다음 숫자를 찾아 간다. 
3. k가 0 이 되었을 때 먹고 있는 음식의 번호를 출력한다. 


이전에 이러한 페턴을 경험 해 본 적이 있다.



'''
