"""
https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=false

새로 들어오는 player의 점수에 따라 점수 매기기

Input
7
100 100 50 40 40 20 10
4
5 25 50 120

Output
6
4
2
1
"""

# Time limit Exceeded!


def climbingLeaderboard(ranked, player):
    answer = []
    r = sorted(set(ranked), reverse=True)
    for p in player:
        if p in set(r):
            answer.append(r.index(p)+1)
        else:
            if p > r[0]:
                answer.append(1)
                r = [p] + r
            elif p < r[-1]:
                answer.append(len(r)+1)
                r = r + [p]
            else:
                r = sorted(set(r+[p]), reverse=True)
                answer.append(r.index(p)+1)
    return answer

# 이진 트리 탐색으로 풀기! 또는 다른 방법 찾기!
