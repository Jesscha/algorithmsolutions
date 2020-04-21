#2019 KAKAO BLIND RECRUITMENT 블록 게임

def solution(board):
    N = len(board)
    cnt = 0
    # 검은게 2개 들었으며 나머지가 모두 같은 숫자인 사각형이 있는지를 확인 하고 그걸0 으로 바꿔 버리는함수
    def check(i, j):
        # print(board)
        bcnt = 0 
        samenumber = 0 
        isFirst = False
        breakFlag = False
        number = 0
        # 세로 상자 확인 
        if i+2 < N and j+1< N:
            for ii in range(i, i+3):
                # print(ii)
                
                for jj in range(j, j+2):
                    if board[ii][jj] == "b":
                        bcnt += 1
                    else:
                        if isFirst:
                            if board[ii][jj] != number:
                                breakFlag = True
                                break
                            else:
                                samenumber += 1
                        else:
                            number = board[ii][jj]
                            samenumber += 1
                            isFirst = True 
                if breakFlag:
                    break
            if bcnt == 2 and samenumber == 4:
                for ii in range(i, i+3):
                    for jj in range(j, j+2):
                        board[ii][jj] = 0
                return True
        if i+1<N and j+2 <N:
            bcnt = 0 
            samenumber = 0 
            isFirst = False
            breakFlag = False
            number = 0
            # 가로 상자 확인 
            for ii in range(i, i+2):
                for jj in range(j, j+3):
                    if board[ii][jj] == "b":
                        bcnt += 1
                    else:
                        if isFirst:
                            if board[ii][jj] != number:
                                breakFlag = True
                                break
                            else:
                                samenumber += 1
                        else:
                            number = board[ii][jj]
                            samenumber += 1
                            isFirst = True 
                if breakFlag:
                    break
            if bcnt == 2 and samenumber == 4:
                for ii in range(i, i+2):
                    for jj in range(j, j+3):
                        board[ii][jj] = 0
                return True
        
        return False
    # 한줄씩 덮어보기 
    executionNumber = 0
    while executionNumber <= 200:
        executionNumber += 1
        for j in range(len(board[0])):
            ii = 0
            # 0이 아닌걸 만날 때까지 내려가서 그 위에 블록을 놓음 
            while ii < N and (board[ii][j] == 0 or board[ii][j] == "b"):
                ii += 1 
            board[ii-1][j] = "b"
        
        #없앨 수 있는 블록이 있는지 확인 
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != 0:
                    if check(i, j):
                        cnt += 1
    answer = cnt
    # print(board)
    return answer


print(solution(	[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0], [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5], [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]))
