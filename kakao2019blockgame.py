#2019 KAKAO BLIND RECRUITMENT 블록 게임
import copy
answer = 0 
newBoard = []
def makeitRain(newBoard):
    tmpBoard = copy.deepcopy(newBoard)
    for j in range(2, len(tmpBoard)-2):
        n = 0
        m = j
        while tmpBoard[n+1][m] == 0:
            n += 1
            if n == len(tmpBoard)-1:
                break
        tmpBoard[n][m] = "g"
        tmpBoard[n-1][m] = "g"
    return tmpBoard

def popCheck(tmpBoard):
    global answer
    flag = True 
    for i in range(2, len(tmpBoard)-2):
        for j in range(2, len(tmpBoard)-2):
            if tmpBoard[i][j] != 0 and tmpBoard[i][j] != "g":
                if isPattern1(i, j, tmpBoard):
                    answer += 1
                    flag = False 
                if isPattern2(i, j, tmpBoard):
                    answer += 1
                    flag = False
                if isPattern3(i, j, tmpBoard):
                    answer += 1
                    flag = False
                if isPattern4(i, j, tmpBoard):
                    answer += 1
                    flag = False
                if isPattern5(i, j, tmpBoard):
                    answer += 1
                    flag = False
    if flag:
        return False
    else:
        return True

def isPattern1(i, j, tmpBoard):
    global newBoard
    # ⌞ 눞혀서
    colorNumber = tmpBoard[i][j]
    if tmpBoard[i][j+1] == "g" and   tmpBoard[i][j+2] == "g" and tmpBoard[i+1][j] == colorNumber and tmpBoard[i+1][j+1] == colorNumber and tmpBoard[i+1][j+2] == colorNumber:
        newBoard[i][j] = 0
        newBoard[i][j+1] = 0
        newBoard[i][j+2] = 0
        newBoard[i+1][j] =0
        newBoard[i+1][j+1] = 0
        newBoard[i+1][j+2] = 0
        return True
        
    return False
def isPattern2(i, j, tmpBoard):
    # ⌏ 눞혀서
    global newBoard
    colorNumber = tmpBoard[i][j]
    if tmpBoard[i][j-1] == "g" and   tmpBoard[i][j-2] == "g" and tmpBoard[i+1][j] == colorNumber and tmpBoard[i+1][j-1] == colorNumber and tmpBoard[i+1][j-2] == colorNumber:
        newBoard[i][j] = 0
        newBoard[i][j-1] = 0
        newBoard[i][j-2] = 0
        newBoard[i+1][j] =0
        newBoard[i+1][j-1] = 0
        newBoard[i+1][j-2] = 0
        return True
        
    return False
    
     
def isPattern3(i, j, tmpBoard):
    # ⌞ 세워서
    global newBoard
    colorNumber = tmpBoard[i][j]
    if tmpBoard[i][j+1] == "g" and   tmpBoard[i+1][j+1] == "g" and tmpBoard[i+1][j] == colorNumber and tmpBoard[i+2][j] == colorNumber and tmpBoard[i+2][j+1] == colorNumber:
        newBoard[i][j] = 0
        newBoard[i][j+1] = 0
        newBoard[i+1][j+1] = 0
        newBoard[i+1][j] =0
        newBoard[i+2][j] = 0
        newBoard[i+2][j+1] = 0
        return True
        
    return False

     
def isPattern4(i, j, tmpBoard):
    #  ⌏ 세워서
    global newBoard
    colorNumber = tmpBoard[i][j]
    if tmpBoard[i][j-1] == "g" and   tmpBoard[i+1][j-1] == "g" and tmpBoard[i+1][j] == colorNumber and tmpBoard[i+2][j] == colorNumber and tmpBoard[i+2][j-1] == colorNumber:
        newBoard[i][j] = 0
        newBoard[i][j-1] = 0
        newBoard[i+1][j-1] = 0
        newBoard[i+1][j] =0
        newBoard[i+2][j] = 0
        newBoard[i+2][j-1] = 0
        return True
        
    return False 
def isPattern5(i, j, tmpBoard):
    # ㅗ 모양
    global newBoard
    colorNumber = tmpBoard[i][j]
    if tmpBoard[i][j-1] == "g" and   tmpBoard[i][j+1] == "g" and tmpBoard[i+1][j] == colorNumber and tmpBoard[i+1][j+1] == colorNumber and tmpBoard[i+1][j-1] == colorNumber:
        newBoard[i][j] = 0
        newBoard[i][j-1] = 0
        newBoard[i][j+1] = 0
        newBoard[i+1][j] =0
        newBoard[i+1][j+1] = 0
        newBoard[i+1][j-1] = 0
        return True
        
    return False




def solution(board):
    global newBoard
    newBoard = [[0 for _ in range(len(board)+4)] for _ in range(len(board)+4)]
    # 0처리를 안하기 위해 padding을 넣어줌
    originboard = copy.deepcopy(board)
    for i in range(len(originboard)):
        for j in range(len(originboard)):
            newBoard[i+2][j+2] = originboard[i][j]
    
    while True:
        tmpBoard  = makeitRain(newBoard)
        if popCheck(tmpBoard) == False:
            break

    return answer


print(solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]))
