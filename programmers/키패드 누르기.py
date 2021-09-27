"""
https://programmers.co.kr/learn/courses/30/lessons/67256

numbers	hand	result
[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	"LRLLLRLLRRL"
[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	"LRLLRRLLLRR"
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	"right"	"LLRLLRLLRL"

"""

def solution(numbers, hand):
    _numbers = [ [1, 4, 7, "*"],
                 [2, 5, 8, 0],
                 [3, 6, 9, "#"] ]
    _where_left = "*"
    _where_right = "#"
    answer = ''

    def _get_distance(a, b):
        for i, nums in enumerate(_numbers):
            if a in nums:
              a_index = [nums.index(a), i]
            if b in nums:
              b_index = [nums.index(b), i]
        _dis = abs(a_index[0]-b_index[0]) + abs(a_index[1]-b_index[1]) 
        return _dis
    
    for num in numbers:
        if num in _numbers[0]:
            _where_left = num
            answer += "L"
        elif num in _numbers[2]:
            _where_right = num
            answer += "R"
        else:
            _l_distance = _get_distance(num, _where_left)
            _r_distance = _get_distance(num, _where_right)
            if _l_distance > _r_distance:
                _where_right = num
                answer += "R"
            elif _l_distance < _r_distance:
                _where_left = num
                answer += "L"
            else:
                if hand == "right":
                    _where_right = num
                    answer += "R"
                else:
                    _where_left = num
                    answer += "L"
            
    return answer