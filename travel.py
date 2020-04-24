from collections import defaultdict
import copy

def solution(tickets):
    countryDict = defaultdict(list)
    for ticket in tickets:
        countryDict[ticket[0]].append(ticket[1] ) 
        countryDict[ticket[0]].sort()
    answer = []
    def dfs(t, footprint, countryDict):
        tmp = footprint[:]
        tmp.append(t)
        if len(tmp) == len(tickets)+1:
            answer.append(tmp)
            return
        for c in countryDict[t]:
            tmpDict = copy.deepcopy(countryDict)
            tmpDict[t].remove(c)
            dfs(c, tmp, tmpDict)
    
    for c in countryDict["ICN"]:
            tmpDict = copy.deepcopy(countryDict)
            tmpDict["ICN"].remove(c)
            dfs(c, ["ICN"], tmpDict)
    return answer[0]

    
print(solution([['ICN', 'COO'], ['ICN', 'BOO'], ['COO', 'ICN'], ['BOO', 'DOO']]))
