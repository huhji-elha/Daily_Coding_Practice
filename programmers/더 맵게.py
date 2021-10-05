"""
https://programmers.co.kr/learn/courses/30/lessons/42626

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

scoville	K	return
[1, 2, 3, 9, 10, 12]	7	2

"""

# 나의 풀이
# python 내장 함수 heapq 사용하기
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    i = 0
    while len(scoville) > 1:
        if scoville[0] < K:
            heapq.heappush(scoville, heapq.heappop(scoville)+heapq.heappop(scoville)*2)
            i += 1
        else:
            return i
    return i if scoville[0]>K else -1