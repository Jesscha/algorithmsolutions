from collections import defaultdict
index = 0
cnt = 0

def checkStation(n, station, w, visit):
    if station - w > 0:
        left = station - w
    else:
        left = 0
    if station + w <= n :
        right = station+w 
    else:
        right = n
    for i in range(left, right+1):
        visit[i] = right+1
    # print(visit)

# 해당 지점에서 출발 했을 때, 0이 아닌 지점을 반환해 주는 함수 
def checkIfPossible(idx, visit, footprint, n):
    global index
    # print(idx)
    if idx >= n:
        return
    if visit[idx] != 0:
        tmp = footprint[:]
        tmp.append(idx)
        checkIfPossible(visit[idx], visit, tmp, n)
    else:
        print(footprint)
        print(visit)
        print(idx)
        for i in footprint:
            visit[i] = idx
            # print(visit[i])
        index = idx
    
        
# 0이 아닌 곳이 주어졌을 때 기지국을 건설하는 함수 
def buildStation(index, visit, w, n, iterCnt):
    global cnt
    if iterCnt > w:
        return 
    if index+w <= n and visit[index+w] == 0:
        checkStation(n, index+w, w, visit)
        cnt += 1
       
    else:
        buildStation(index-1, visit, w, n, iterCnt +1 )
    
def solution(n, stations, w):
    global index, cnt
    # visit을 dict로 대신 하면 더 빠르지 않을까
    visit = defaultdict(lambda : 0)
    for station in stations:
        checkStation(n, station, w, visit)
    
    while index <= n:
        # index는 visit에서 0 인 것만 가르킨다.
        checkIfPossible(index, visit, [], n)
        # 0인 자리를 시작으로 타워를 지어서 0을 채운다.
        buildStation(index, visit, w, n, 0)
        index += 1
    
    return cnt
            
    
    
print(solution(16, [9], 2))    



'''
제일 무식한 방법으로 풀 수 있는게 뭐가 있지

1. 주어진 곳 주변을 다 visit 한다. visit 할때는 해당 visit의 오른쪽 끝 번호를 적는다
2. 이미 비짓한 곳을 방문하는 경우 인덱스를 오른쪽 끝 번호 더하기 1번으로 옮긴다.
3. 거기도 이미 방문한 곳일 경우에 인덱스를 오른쪽 끝 번호 더하기 1번으로 옮긴다. 
4. 0인 경우에 W 만큼 뒤 위치 전파국을 짓는다. 이 위치가 visit == 0 이 아니라면 그 왼쪽에, 아니라면 그 왼쪽에 전파국을 짓는다.
5. 지어진 전파국의 개수를 센다. 



'''