def solution(k, room_number):
    rooms = [0 for _ in range(k+1)]
    answer = []

    for room in room_number:
        n = room
        visit = [n]
        while rooms[n] != 0:
            n = rooms[n]
            visit.append(n)
        answer.append(n)
        for i in visit:
            rooms[i] = n+1 
    return answer