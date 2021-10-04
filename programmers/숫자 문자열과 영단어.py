"""
https://programmers.co.kr/learn/courses/30/lessons/81301

s	             result
"one4seveneight"	1478
"23four5six7"	234567
"2three45sixseven"	234567
"123"	123
"""

# 나의 풀이 
def solution(s):
    _alphabet = ['zero', 'one', 'two', 'three', 'four',
               'five','six','seven','eight','nine']
    for i, word in enumerate(_alphabet):
        s = s.replace(word, str(i))
    return int(s)