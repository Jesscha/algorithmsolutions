def solution(jobs):
    jobs.sort(key = lambda x: x[1])
    curT = 0
    ansset = [] 
    while jobs:
        isNotIn = True
        for i in range(len(jobs)):
            if jobs[i][0] <= curT:
                excution = jobs.pop(i)
                isNotIn = False
                break
        if isNotIn:
            curT += 1 
        else:
            curT += excution[1]
            ansset.append(curT-excution[0])
    answer = sum(ansset)//len(ansset)
    return answer

print(solution([[0, 3], [1, 9], [2, 6]]))


'''
어떻게 푸는 문제인가

문제의 정의, 주어지는 배열에는 요청시간과 수행하는데 걸리는 시간이 들어있다. 

한번에 하나의 작업밖에 할 수 없다. 

큐에 넣고 작업을 수행하면 되지 않을까? 

풀이방법 

작업이 긴게 앞에 올수록 다른 대기 업무의 작업시간도 같이 배로 늘어난다는 단점이 있다. 

작업 가능한 것들 중에서 작업 시간이 가장 짧은 것을 수행하고 시간을 체크하는 알고리즘을 만들어야 한다. -> 일단 전체를 수행시간 짧은 순으로 정렬 해 놓고 작업시간 해당하는걸 처음 만나면 작업을 수행시키도록 하면 되지 않을까? 

현재 시간을 체크하는 변수를 만들고 curT = 0 

curT보다 요청시간이 같거나 빠른 것 중 제일 작업 시간이 짧은걸 수행 시킨다. 

해당 작업의 curT - 요청시간이 anset 에 추가 된다. 

해당 작업 수행시간 만큼 curT를 증가시킨다. 

만약 수행할수 있는 작업이 없으면, curT를 1 증가시킨다.

'''
