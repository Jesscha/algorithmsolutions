def solution(s):
    answer = []
    numberList = []
    s = s.lstrip('{').rstrip("}").split('},{')
    for i in s:
        numberList.append(i.split(","))
    numberList.sort(key = len)
    answer = [] 
    for numbers in numberList:
        for num in numbers:
            if num not in answer:
                answer.append(num)
    return answer

print(solution("{{20,111},{111}}"))