def solution(k, room_number):
    rooms = [0 for i in range(k+1)]
    answer = []
    for i in room_number:
        if rooms[i] == 0:
            if rooms[i+1] ==0:
                rooms[i] = i+1
                answer.append(i)
            else:
                footprint = [i]
                # 점거 당하지 않은 방이 나올때까지 탐색하며 흔적 수집 
                n = i+1
                while rooms[n] !=0:
                    footprint.append(n)
                    n += 1
                answer.append(n-1)
                # 흔적에 들어 있던 모든 것들을 전부 처음 만나는 0이 있는 곳을 가리키게 함                 
                for index in footprint:
                    rooms[index] = i+1
        else:
            if rooms[rooms[i]] == 0:
                if rooms[rooms[i]+1] ==0:
                    rooms[rooms[i]] = rooms[i]+1
                    answer.append(rooms[i])
                else:
                    footprint = [rooms[i]]
                # 점거 당하지 않은 방이 나올때까지 탐색하며 흔적 수집 
                    n = rooms[i]+1
                    while rooms[n] !=0:
                        footprint.append(n)
                        n += 1
                    answer.append(n-1)
                # 흔적에 들어 있던 모든 것들을 전부 처음 만나는 0이 있는 곳을 가리키게 함                 
                    for index in footprint:
                        rooms[index] = i+1
            else:
                footprint = [rooms[i]]
                # 점거 당하지 않은 방이 나올때까지 탐색하며 흔적 수집 
                n = rooms[i]+1
                while rooms[n] !=0:
                    footprint.append(n)
                    n += 1
                answer.append(n-1)
                # 흔적에 들어 있던 모든 것들을 전부 처음 만나는 0이 있는 곳을 가리키게 함                 
                for index in footprint:
                    rooms[index] = i+1
    print(rooms)
    return answer

'''
전략 떠올리기

이미 사람이 차 있는 방은 그방에 다음 사람이 왔을 때 어디로 가야 하는지에 대한 정보를 담고 있어야 한다. 

이걸 어떻게 구현할 것인가?

1. 각 방의 빈 공간을 만든다.
2. 빈 공간이 비어 있다면, 그냥 넣는다. 넣을때, 그 자리에 오는 다음 사람이 들어가야 할 곳을 가르키는 숫자를 넣는다. 
    - 일단 바로 옆을 보고, 바로 옆에 이미 사람이 차 있으면  그 차있는 방의 옆을보고 .... 을 반복한다. 
    - 이 때 거쳐간 방들을 모두 기록해 놓는다. 
    - 마침내 가야 할 방을 찾았을 때, 그 방에 사람을 배치하고 그사람 옆에 사람이 차 있으면 위의 과정을 반복한다. 
    - 비어있는 자리를 찾으면 그 방의 자리를 지금껏 지나쳐 온 모든 방들에 대해서 업데이트 한다. 
3. 가려는 방이 차 있으면 그 방이 가르키는 번호로 간다 위의 과정을 반복한다. 


옆을 보고 체크를 하는 함수를 어떻게 구현할 것인가??

while place != 0:
    ...
    ...
    ...
    place = 00
update all rooms in footprint





'''