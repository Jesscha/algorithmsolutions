''' 2018 KAKAO BLIND RECRUITMENT [3차] 방금그곡 '''
def hashToOther(melody):
    melody = melody.replace("C#", "Z")
    melody = melody.replace("D#", "X")
    melody = melody.replace("F#", "M")
    melody = melody.replace("G#", "L")
    melody = melody.replace("A#", "P")
    return melody


def solution(m, musicinfos):
    # 조건을 만족하는 답이 모이는 곳 
    ansset = []
    m = hashToOther(m)
    for idx, musicinfo in enumerate(musicinfos):
        st, ed, mName, melody = musicinfo.split(',')
        playTime = int(ed[:2])*60 + int(ed[3:5]) - int(st[:2])*60 - int(st[3:5])
        
        melody = hashToOther(melody)
        
        if len(melody) < playTime:
            melody = melody*(playTime//len(melody)) + melody[:(playTime%len(melody))]
        elif len(melody) > playTime:
            melody = melody[:(playTime%len(melody))]
        else:
            melody = melody
        if m in melody:
            ansset.append([mName, playTime, idx])
    
    
    
    if ansset:
        ansset.sort(key = lambda x: (-x[1], idx))
        return ansset[0][0]
    else:
        return "(None)"


print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))




''' 풀이 아이디어 정리 

기억하고 있는 멜로디가 주어진 멜로디 안에 있는지를 판별하는 문제 

시작, 종료 시간을 바탕으로 재생 시간을 구한다.

주어진 멜로디의 길이가 재생 시간보다 짧은 경우 해당 시간 만큼 반복된 멜로디가 뒤에 추가된다. 

주어진 멜로디의 길이가 재생 시간보다 긴 경우 해당 시간만큼 멜로디를 자른다. 

기억하고 있는 멜로디가 포함되어 있는 멜로디를 찾는다. 이때, C와 C#은 다르다는 점을 고려 해야 한다. 그냥 in을 쓰면 이를 구분하지 못하게 된다. (처음부터 # 문자를 다른걸로 치환하는게 좋을 듯 하다.)

답이 여러개인 경우, 재생시간이 긴 것을 먼저, 재생 시간도 같은경우, 먼저나온 것으로 한다 


'''