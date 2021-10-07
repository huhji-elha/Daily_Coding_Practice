"""
https://programmers.co.kr/learn/courses/30/lessons/64061

NxN 칸에서 moves 순서대로 인형을 뽑은 뒤 basket에 넣기
basket에서 인접한 인형은 사라진다.

board	moves	result
[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	[1,5,3,5,1,2,1,4]	4

"""
# 나의 풀이
# board 2중 배열을 뒤집은 뒤 1 이상의 값만 한번더 뒤집기
def solution(board, moves):
    board = list(map(list, zip(*board)))
    basket, board2 = [], []

    for b in board:
        b_index = len(b)
        for i in range(len(b)):
            if b[i] > 0:
                b_index = i
                break
        board2.append(b[b_index:][::-1])

    answer = 0
    for c in moves:
        if len(board2[c-1]) > 0:
            doll = board2[c-1].pop()
        else:
            continue
        if len(basket) > 0 and basket[-1] == doll:
            answer += 1
            basket.pop()
        else:
            basket.append(doll)
    return answer*2

# 코드 더 깔끔하게 다듬기
# lambda 사용해서 배열 뒤집는 걸 전부 한 줄에 처리
def solution(board, moves):
    board = list(map(lambda x:list(filter(lambda y:y>0, x))[::-1], zip(*board)))
    answer, basket = 0, []

    for c in moves:
        if len(board[c-1]) > 0:
            doll = board[c-1].pop()
        else:
            continue
        if len(basket) > 0 and basket[-1] == doll:
            answer += 1
            basket.pop()
        else:
            basket.append(doll)
    return answer*2