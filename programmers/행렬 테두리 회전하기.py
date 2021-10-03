"""
https://programmers.co.kr/learn/courses/30/lessons/77485

행렬의 세로 길이(행 개수) rows, 가로 길이(열 개수) columns, 그리고 회전들의 목록 queries가 주어질 때, 각 회전들을 배열에 적용한 뒤, 
그 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자들을 순서대로 배열에 담아 return 하도록 solution 함수를 완성해주세요.
rows	columns	queries	result
6	6	[[2,2,5,4],[3,3,6,6],[5,1,6,3]]	[8, 10, 25]
3	3	[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]	[1, 1, 5, 3]
100	97	[[1,1,100,97]]	[1]
"""


# 나의 풀이
# 직사각형의 테두리를 왼쪽 상단을 중심으로 시계방향으로 리스트로 바꾸기
# 회전한(뒤로 한칸씩 밀린) 리스트를 재배치

def solution(rows, columns, queries):
    answer, l, arr = [], [], []
    for i in range(1,rows*columns+1):
        l.append(i)
        if i%columns == 0:
            arr.append(l)
            l = []

    def _get_border(queries):
        border_arr = []
        for i in range(queries[1], queries[3]):
            border_arr.append((queries[0]-1, i))
        for i in range(queries[0], queries[2]):
            border_arr.append((i, queries[3]-1))
        for i in range(queries[3]-1,queries[1]-1,-1):
            border_arr.append((queries[2]-1, i-1))
        for i in range(queries[2]-1, queries[0]-1, -1):
            border_arr.append((i-1, queries[1]-1))
        return border_arr

    for query in queries:
        border = _get_border(query)
        border.append(border[0])
        _change = [arr[i[0]][i[1]] for i in border[:-1]]
        for i,z in zip(border[1:], _change):
            arr[i[0]][i[1]] = z
        answer.append(min(_change))

    return answer