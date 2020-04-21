def solution(n, k):
    import math as m 
    numList = list(range(1, n+1))
    answerList = []
    while n > 0:
        n -= 1
        p, r= divmod(k, m.factorial(n))
        if r == 0:
            p-= 1
        answerList.append(numList[p])
        numList.remove(numList[p])
        k = r 
    return answerList