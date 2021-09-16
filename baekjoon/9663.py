# 백트래킹 - NQueen
import sys 
n = int(sys.stdin.readline())

board = []

# 배열 두 개로 풀면 X
# 1차원 배열에서 x,y 좌표를 index, board[index]로 풀어야한다.
# 0,0을 표현하면 board[0] = 0

cnt = 0
for i in range(n):
    if board[i] 




# _board = [[0]*n for _ in range(n)]

# i, j = 3, 4

# def _left_diag(arr,i,j):
#     global n
#     if i > j: 
#         _i, _j = i-j, 0
#     else: 
#         _i, _j = 0, j-i
#     ii = 0
#     while True:
#         arr[_i+ii][_j+ii] = 1
#         ii += 1
#         if _i+ii > n-1 or _j+ii > n-1:
#             break

# def _right_diag(arr,i,j):
#     global n
#     if i+j < n:
#         i_, j_ = 0, i+j
#     else:
#         i_, j_ = i-(n-1-j), n-1
#     ii = 0
#     while True:
#         arr[i_+ii][j_-ii] = 1
#         ii += 1
#         if i_+ii > n-1 or j_-ii < 0:
#             break

# def _get_queen_arr(arr, i, j, _flag):
#     global n
#     for _i in range(n):
#         arr[i][_i] = _flag 
#         arr[_i][j] = _flag 
#     _left_diag(arr, i, j)
#     _right_diag(arr, i, j)
    

# Nqueen = 0
# def N_Queen(n):
#     cnt = 0
#     chess_board = [[0]*n for _ in range(n)]
    
#     def get_n_queen(chess_board, cnt):
#         global Nqueen
#         if cnt == n:
#             Nqueen += 1
#             print("done")
#             return
#         for a in range(n):
#             for b in range(n):
#                 if chess_board[a][b] == 0:
#                     cnt += 1
#                     _get_queen_arr(chess_board, a, b, 1)
#                     print(a, b)
#                     print("cnt : ", cnt)

#                     get_n_queen(chess_board, cnt)
#                     _get_queen_arr(chess_board, a, b, 0)
                    
#                     chess_board[a][b] = 1
#                     cnt = 0
#                     for ch in chess_board:
#                         print(ch)
#                     print("N queen : ", Nqueen)
#     get_n_queen(chess_board, cnt)

# N_Queen(n)
# # for b in _board:
#     # print(b)    
# print(Nqueen)

             
