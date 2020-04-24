from collections import defaultdict

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
            tmpDict = countryDict.copy()
            tmpDict[t].remove(c)
            dfs(c, tmp, tmpDict)
            tmpDict[t].append(c)
            tmpDict[t].sort()
    
    for c in countryDict["ICN"]:
            tmpDict = countryDict.copy()
            tmpDict["ICN"].remove(c)
            dfs(c, ["ICN"], tmpDict)
            tmpDict["ICN"].append(c)
            tmpDict["ICN"].sort()
    return answer[0]

    
print(solution([['ICN', 'COO'], ['ICN', 'BOO'], ['COO', 'ICN'], ['BOO', 'DOO']]))
