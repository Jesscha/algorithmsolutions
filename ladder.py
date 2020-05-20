from collections import deque, defaultdict
import math
import sys
sys.setrecursionlimit(10**6)

def bfs(land, height, visited, position, group):
    dirs = [(0,1), (1,0),(-1,0), (0,-1)] 
    queue = deque()
    queue.append(position)
    while queue:
        y, x = queue.popleft()
        visited[y][x] = group
        for dy, dx in dirs:
            ny = y + dy 
            nx = x + dx
            if 0 <= ny < len(land) and 0 <= nx < len(land) and visited[ny][nx] == 0 and abs(land[ny][nx]-land[y][x])<= height:
                visited[ny][nx] = group
                queue.append((ny,nx))
def find_height(table, visited, land, height): 
    for y in range(len(land)):
        for x in range(len(land[0])):
            rx = x + 1
            ny = y + 1
            if rx < len(land[0]) and visited[y][x] != visited[y][rx] :
                a = min(visited[y][x], visited[y][rx])
                b = max(visited[y][x], visited[y][rx])
                table[(a,b)] = min(table[(a,b)], abs(land[y][x]-land[y][rx]))
            if ny < len(land) and visited[y][x] != visited[ny][x] :
                a = min(visited[y][x], visited[ny][x])
                b = max(visited[y][x], visited[ny][x])
                table[(a,b)] = min(table[(a,b)], abs(land[y][x]-land[ny][x]))

def find_parent(x, parent):
    if parent[x] == x:
        return x
    else:
        p = find_parent(parent[x], parent)
        parent[x] = p
        return p

def unioin_find(x, y, parent):
    a = find_parent(x, parent)
    b = find_parent(y, parent)
    parent[b] = a




def solution(land, height):
    visited = [[0 for _ in range(len(land[0]))] for _ in range(len(land))] 

    group = 1 
    for y in range(len(land)):
        for x in range(len(land[0])):
            if visited[y][x] == 0 :
                bfs(land, height, visited, (y,x), group)
                group += 1

    table = defaultdict(lambda : math.inf)
    find_height(table, visited, land, height)
    table = sorted(table.items(), key=lambda x: x[1])


    answer = 0
    nodes = {i:i for i in range(1, group)}
    print(nodes)

    for (a, b), value in table:
        if find_parent(a, nodes) != find_parent(b, nodes):
            unioin_find(a, b, nodes)
            answer += value


    
    return answer

print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1))