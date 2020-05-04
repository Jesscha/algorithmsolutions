
ansset = []
cnt = 0
from collections import defaultdict
def solution(user_id, banned_id):
    idDict = defaultdict(set)
    
    for banid in banned_id:
        for uid in user_id:
            if len(banid) == len(uid):
                flag = True
                for i in range(0,len(banid)):
                    if banid[i] == "*":
                        continue
                    else:
                        if banid[i] != uid[i]:
                            flag = False
                            break
                if flag: idDict[banid].add(uid)
    keys  = [ k for k  in banned_id]
    # print(idDict)
    def dfs(keyIndex, footprint):
        global ansset, cnt
        if keyIndex == len(keys):
            if len(footprint) == len(banned_id):

                ansset.append(set(footprint))
                cnt += 1
            return 
        for j in idDict[keys[keyIndex]]:
            if j not in footprint:
                tmpFoot = footprint[:]
                tmpFoot.append(j)
                dfs(keyIndex+1, tmpFoot)

    dfs(0, [])
    
    answer = []
    for i in ansset:
        if i in answer:
            continue
        answer.append(i)

    return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))