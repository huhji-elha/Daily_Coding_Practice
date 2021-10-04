"""
https://programmers.co.kr/learn/courses/30/lessons/76501

absolutes	signs	result
[4,7,12]	[true,false,true]	9
[1,2,3]	[false,false,true]	0
"""

# 나의 풀이
# zip을 이용해 풀기
def solution(absolutes, signs):
    answer = 0
    for _abs, _sign in zip(absolutes, signs):
        _int = _abs if _sign else -_abs
        answer += _int
    return answer