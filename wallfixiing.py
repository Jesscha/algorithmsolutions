from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1
    weak_length = len(weak)
    # 1 원형 문제를 해결하기 
    for i in range(weak_length):
        weak.append(weak[i]+n)

    #2  가능한 모든 춟발지점 구하기 
    for i in range(weak_length):
        possible_starting_points = [weak[j] for j in range(i, i+weak_length)]

        # 3 가능한 친구 순서 모두 구하기 
        candidates = permutations(dist, len(dist))
      
        # 4 모든 친구가 모든 출발점에서 출발하는 경우 필요한 친구의 수 세기
        for friends in candidates:
            # 사용한 친구 수
            friend_number = 1 
            # 사용한 친구의 인덱스
            friend_idx = 0 
            # 친구가 커버할 수 있는거리 
            max_length = possible_starting_points[0] + friends[friend_idx]

            for idx in range(weak_length):
                # 다음에 가야할 좌표가 커버해야 하는 거리보다 멀리 있으면
                if possible_starting_points[idx] > max_length:
                    # 사람 수 늘리고 
                    friend_number += 1 
                    # 사람수 초과면 중지
                    if friend_number > len(dist):
                        break
                    # 친구도 다음 친구로 이전 
                    friend_idx += 1
                    # 새로운 친구와 새로운 출발 지점으로 커버 가능 거리 갱신
                    max_length = possible_starting_points[idx] + friends[friend_idx]
            answer = min(answer, friend_number)
    if answer > len(dist):
        return -1
    return answer

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))



'''
https://inspirit941.tistory.com/entry/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-recruit-%EC%99%B8%EB%B2%BD-%EC%A0%90%EA%B2%80-Level-3 
의 풀이를 참고하였음 

문제 해결 방법

1. 원형 문제를 해결 한다. => 길이를 두배로 늘리고 붙여 버리면 된다. 

2. 가능한 모든 출발 지점을 구한다. 

3. 가능한 모든 사용 인원을 구한다.

4. 가능한 모든 사용인원이 가능한 모든 출발지점에서 출발을 했을때 몇 명이 필요한지 센다. 

5. 모든 경우가 지나고 제일 작은걸 정답으로 삼는다. 

6. 만약 주어진 사람 수 보다 쓰여진 사람수가 많다면 불가능하단 말이므로 -1

'''