"""
https://leetcode.com/problems/reconstruct-itinerary

[from, to]로 구성된 항공권 목록을 이용해 JFK에서 출발하는 여행 일정 구성하기.
여러 일정이 있는 경우 어휘 순으로 방문한다.

Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
"""

# 아이디어01 : while문과 재귀 함수를 사용해서 트리의 끝까지 도달한 다음 리스트에 담기
# while문을 빠져나온 순서대로(더 이상 여행할 곳이 없는 마지막 여행지 순서대로) 리스트에 담겼으므로
# return할 때 리스트를 뒤집어주어야한다.
# Runtime : 144 ms
# Memory : 14.7 MB
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticket_dict = defaultdict(list)
        for t in sorted(tickets, reverse=True):
            ticket_dict[t[0]] += [t[1]]

        def reconstruct(start_t):
            while ticket_dict[start_t]:
                next_t = ticket_dict[start_t].pop()
                reconstruct(next_t)
            answer.append(start_t)

        answer = []
        reconstruct("JFK")
        return answer[::-1]


"""
reconstruct의 start_t와 next_t의 출력 순서를 확인해보면 다음과 같다.
ticket_dict = {'NRT': ['JFK'], 'JFK': ['NRT', 'KUL']}

next_t:  KUL
start_t:  KUL
next_t:  NRT
next_t:  JFK
start_t:  JFK
start_t:  NRT
start_t:  JFK
"""
