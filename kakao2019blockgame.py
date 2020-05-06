#2019 KAKAO BLIND RECRUITMENT 블록 게임
import numpy as np 


def solution (board):
    board = np.array(board)
    answer = 0 
    blocks = {}
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col > 0:
                if col not in blocks:
                    blocks[col] = {
                            "left": 51, 
                            "right": -1,
                            "top": 51, 
                            "bottom": -1,
                            "coords": []
                                   }
                blocks[col]["left"] = min(blocks[col]["left"], j)
                blocks[col]["right"] = max(blocks[col]["right"], j)
                blocks[col]["top"] = min(blocks[col]["top"], i)
                blocks[col]["bottom"] = max(blocks[col]["bottom"], i)
                blocks[col]["coords"].append([i, j])
        
        
        removed =1 
        while removed > 0:
            removed = 0
            for block_key in blocks:
                can_remove = True
                block = blocks[block_key]
                zeros = 0
                for i in range(block["top"], block["bottom"]+1):
                # 왼쪽에서 오른쪽 까지
                    print(i)
                    for j in range(block["left"], block["right"]+1):
                        if board[i][j] == 0:
                            zeros += 1
                            if (board[:i,j] > 0).any():
                                can_remove = False
                                break
                    if not can_remove:
                        break
                if can_remove and zeros == 2:
                    for coord in blocks[block_key]["coords"]:
                        board[coord[0]][coord[1]] = 0
                    del blocks[block_key]

                    removed += 1
                    answer += 1
                    break
    return answer


print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [
      0, 0, 0, 0, 0, 4, 4, 0, 0, 0], [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5], [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]))




# import copy
# answer = 0
# newBoard = []
# def makeitRain(newBoard):
#     tmpBoard = copy.deepcopy(newBoard)
#     for j in range(2, len(tmpBoard)-2):
#         n = 0
#         m = j
#         while tmpBoard[n+1][m] == 0:
#             n += 1
#             if n == len(tmpBoard)-1:
#                 break
#         tmpBoard[n][m] = "g"
#         tmpBoard[n-1][m] = "g"
#     return tmpBoard

# def popCheck(tmpBoard):
#     global answer
#     flag = True
#     for i in range(2, len(tmpBoard)-2):
#         for j in range(2, len(tmpBoard)-2):
#             if tmpBoard[i][j] != 0 and tmpBoard[i][j] != "g":
#                 if isPattern1(i, j, tmpBoard):
#                     answer += 1
#                     flag = False
#                 if isPattern2(i, j, tmpBoard):
#                     answer += 1
#                     flag = False
#                 if isPattern3(i, j, tmpBoard):
#                     answer += 1
#                     flag = False
#                 if isPattern4(i, j, tmpBoard):
#                     answer += 1
#                     flag = False
#                 if isPattern5(i, j, tmpBoard):
#                     answer += 1
#                     flag = False
#     if flag:
#         return False
#     else:
#         return True

# def isPattern1(i, j, tmpBoard):
#     global newBoard
#     # ⌞ 눞혀서
#     colorNumber = tmpBoard[i][j]
#     if tmpBoard[i][j+1] == "g" and   tmpBoard[i][j+2] == "g" and tmpBoard[i+1][j] == colorNumber and tmpBoard[i+1][j+1] == colorNumber and tmpBoard[i+1][j+2] == colorNumber:
#         newBoard[i][j] = 0
#         newBoard[i][j+1] = 0
#         newBoard[i][j+2] = 0
#         newBoard[i+1][j] =0
#         newBoard[i+1][j+1] = 0
#         newBoard[i+1][j+2] = 0
#         return True

#     return False
# def isPattern2(i, j, tmpBoard):
#     # ⌏ 눞혀서
#     global newBoard
#     colorNumber = tmpBoard[i][j]
#     if tmpBoard[i][j-1] == "g" and   tmpBoard[i][j-2] == "g" and tmpBoard[i+1][j] == colorNumber and tmpBoard[i+1][j-1] == colorNumber and tmpBoard[i+1][j-2] == colorNumber:
#         newBoard[i][j] = 0
#         newBoard[i][j-1] = 0
#         newBoard[i][j-2] = 0
#         newBoard[i+1][j] =0
#         newBoard[i+1][j-1] = 0
#         newBoard[i+1][j-2] = 0
#         return True

#     return False


# def isPattern3(i, j, tmpBoard):
#     # ⌞ 세워서
#     global newBoard
#     colorNumber = tmpBoard[i][j]
#     if tmpBoard[i][j+1] == "g" and   tmpBoard[i+1][j+1] == "g" and tmpBoard[i+1][j] == colorNumber and tmpBoard[i+2][j] == colorNumber and tmpBoard[i+2][j+1] == colorNumber:
#         newBoard[i][j] = 0
#         newBoard[i][j+1] = 0
#         newBoard[i+1][j+1] = 0
#         newBoard[i+1][j] =0
#         newBoard[i+2][j] = 0
#         newBoard[i+2][j+1] = 0
#         return True

#     return False


# def isPattern4(i, j, tmpBoard):
#     #  ⌏ 세워서
#     global newBoard
#     colorNumber = tmpBoard[i][j]
#     if tmpBoard[i][j-1] == "g" and   tmpBoard[i+1][j-1] == "g" and tmpBoard[i+1][j] == colorNumber and tmpBoard[i+2][j] == colorNumber and tmpBoard[i+2][j-1] == colorNumber:
#         newBoard[i][j] = 0
#         newBoard[i][j-1] = 0
#         newBoard[i+1][j-1] = 0
#         newBoard[i+1][j] =0
#         newBoard[i+2][j] = 0
#         newBoard[i+2][j-1] = 0
#         return True

#     return False
# def isPattern5(i, j, tmpBoard):
#     # ㅗ 모양
#     global newBoard
#     colorNumber = tmpBoard[i][j]
#     if tmpBoard[i][j-1] == "g" and   tmpBoard[i][j+1] == "g" and tmpBoard[i+1][j] == colorNumber and tmpBoard[i+1][j+1] == colorNumber and tmpBoard[i+1][j-1] == colorNumber:
#         newBoard[i][j] = 0
#         newBoard[i][j-1] = 0
#         newBoard[i][j+1] = 0
#         newBoard[i+1][j] =0
#         newBoard[i+1][j+1] = 0
#         newBoard[i+1][j-1] = 0
#         return True

#     return False



# def solution(board):
#     global newBoard
#     # 0처리를 안하기 위해 padding을 넣어줌
#     newBoard = [[0 for _ in range(len(board)+4)] for _ in range(len(board)+4)]
    
#     originboard = copy.deepcopy(board)
#     for i in range(len(originboard)):
#         for j in range(len(originboard)):
#             newBoard[i+2][j+2] = originboard[i][j]

#     while True:
#         tmpBoard  = makeitRain(newBoard)
#         if popCheck(tmpBoard) == False:
#             break

#     return answer

