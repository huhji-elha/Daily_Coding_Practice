"""
https://programmers.co.kr/learn/courses/30/lessons/77484

lottos                   	win_nums	       result
[44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19]	[3, 5]
[0, 0, 0, 0, 0, 0]	[38, 19, 20, 40, 15, 25]	[1, 6]
[45, 4, 35, 20, 3, 9]	[20, 9, 3, 45, 4, 35]	[1, 1]
"""

# 원래 풀이
def solution(lottos, win_nums):
    _min = 0
    _zeros = 0 # count 함수로 대체할 수 있다. 하지만 이럴 경우 loop을 두 번 사용하는게 아닐까?
    for l in lottos:
        if l in win_nums:
          _min += 1
        if l == 0:
          _zeros += 1
    
    # 해당 함수를 배열로 대체할 수 있다.
    def get_score(num):
      return 7-num if num > 0 else 6
    
    return [get_score(_min+_zeros), get_score(_min)]


# 배열로 풀이하기
def solution2(lottos, win_nums):
    _min = 0
    score = [6,6,5,4,3,2,1]
    _zeros = lottos.count(0)
    for l in lottos:
        if l in win_nums:
            _min += 1
    return score[_min+_zeros], score[_min]
    