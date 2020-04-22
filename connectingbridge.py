import heapq as hq

def solution(n, costs):
    answer = 0
    costList = [[] for _ in range(n)]

    for f, t, c in costs:
        costList[f].append((t,c))
        costList[t].append((f,c))
    workList = [] 
    visit = [0]*n

    hq.heappush(workList, (0,0))
    while 0 in visit:
        c, p = hq.heappop(workList)
        if visit[p]:
            continue
        answer += c
        visit[p] = 1

        for t, c in costList[p]:
            if visit[t] == 0:
                hq.heappush(workList, (c, t))
            
    return answer
print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))


'''

주어진 배열을 정리한다

위의 방법대로 하면, 힙안에 코스트는 계속 남아있고 비짓을 한 경우 그건 무시를 하게 되기 때문에 워킹하는 코드가 된다. 

구현 방법

일단 빈 리스트를 만든다.

주어진 코스트를 바탕으로 각 리스트에 원소를 추가한다 원소는 (갈수있는 곳, 가격)이다. 

heapq용 리스트 만들고 거기에 (0,0)을 푸시한다. 

새롭게 들어온 것의 첫번째 원소를 visit 처리 한다. 

리스트 상에 해당 원소 for 문을 돌린다. 방문 하지 않은 것들을 heapq에 담는다. 코스트가 먼저 들어가게 해야 heapq정렬이 빠르게 잘 됨 

만약 visit이 모두 되었으면 종료한다. 




'''