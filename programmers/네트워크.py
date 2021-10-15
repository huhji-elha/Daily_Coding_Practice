"""
컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 
네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

n = 3
computers = [[1, 1, 0], 
             [1, 1, 1], 
             [0, 1, 1]]
             
n = 4
computers = [[1,0,1,0],
             [0,1,0,1],
             [1,0,1,0],
             [0,1,0,1]]
"""

# 나의 풀이
# used 집합을 만들어서 한번 거친 node를 저장
# DFS 방식으로 풀이
def solution(n, computers):
    answer, used = 0, set()
    def network(idx):
        for j,c in enumerate(computers[idx]):
            if j not in used:
                if c:
                    used.add(j)
                    network(j)

    for i in range(n):
        if i not in used:
            used.add(i)
            network(i)
            answer += 1
        else:
            continue
    return answer