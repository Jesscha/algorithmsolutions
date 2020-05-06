def solution(food_times, k):

    food_times_list = []
    totalTime = 0
    for i in range(0, len(food_times)):
        food_times_list.append([i, food_times[i]])
        totalTime+=food_times[i]

    if totalTime <= k:
        return -1

    food_times_list = sorted(food_times_list, key=lambda x:x[1])
    # 첫번째 꺼에 길이를 곱한 것 즉, 가장 양이 적은 놈을 먹어 치울 때까지 걸리는 시간 
    delTime = food_times_list[0][1]*len(food_times_list)
    i=1
    # print k
    # print delTime
    # 가장 적은 양을 다 먹어 치울 때까지 걸리는 시간이 k보다 작으면
    while delTime < k:
        k-=delTime # k에서 delTime을 뺀다. 
        delTime = (food_times_list[i][1]-food_times_list[i-1][1])*(len(food_times_list)-i) # deltime을 그다음 짭은 놈 만큼 뺀다
        # print k, delTime
        i+=1 # i를 1개 더한다. 
    # 남은 음식들 배치, 원래 번호순으로
    food_times_list = sorted(food_times_list[i-1:], key=lambda x:x[0])
    # print food_times_list
    # print k
    return food_times_list[k%len(food_times_list)][0]+1 # 
    # k가 남았으니까 남은만큼은 한줄씩 먹어줘야 함 그리고 남은 음식이 먹어야 할  음식 
    
