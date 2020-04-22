# 베스트 엘범 
from collections import defaultdict

def solution(genres, plays):
    gDict = defaultdict(list)
    for i in range(len(genres)):
        gDict[genres[i]]  = [[],0]
    for i in range(len(plays)):
        gDict[genres[i]][0].append((i, plays[i]))
        gDict[genres[i]][1] += plays[i]
    ansset = [] 
    answer = []
    for k in gDict:
        ansset.append((k,gDict[k]))
    ansset.sort(key = lambda x: x[1][1], reverse= True)
    for song in ansset:
        song[1][0].sort(key=lambda x: (-x[1], x[0]))
        if len(song[1][0]) >= 2:
            answer.append(song[1][0][0][0])
            answer.append(song[1][0][1][0])
        else:
            answer.append(song[1][0][0][0])    
    return answer

print(solution(	["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

'''

dict[genre] = [[[0,200],[1,300], [3,200]], 전체합]

장르별로 노래의 인덱스를 포함시킨다. 

장르별로 전체 재생 회수를 합한다.

장르를 총합을 기준으로 정렬, 새로운 리스트를 만들면 될듯


'''