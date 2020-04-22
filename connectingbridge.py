

def solution(n, costs):
    answer = []
    graph = [[0 for _ in range(n)] for _ in range(n)] 
    visit = [0 for _ in range(n)]


    for cost in costs:
        graph[cost[0]][cost[1]] = cost[2]
        graph[cost[1]][cost[0]] = cost[2]
    print(graph)

    def dfs(p, c, v):
        if v == []:
            v = []
        if len(v) == n :
            print(v)
            answer.append(c)
        for i in range(len(graph[p])):
            # print(graph[p][i])
            # print(v[i])
            if graph[p][i] != 0 and i not in v:
                c += graph[p][i]
                v.append(i)
                dfs(i, c, v)
    
    dfs(0, 0, [0])
    
    
    return answer
print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))


'''

브루트 포스 로 풀수 있지 않나?

전체 그래프 관계를 그리고 거기에 맞춰서 탐색을 하면 되지 않나 

dfs로 만들어야 겠네 

과재 1 주어진 costs를 그래프로 만들기 

[i][j] 에 코스트가 적혀있다. 

과제 2 dfs를 돌리기 

visit과 cost, position을 인자로 받음 

visit에 더 방문할 곳이 없으면 종료,cost 반환 


'''