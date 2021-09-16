"""
주어진 문자열을 정수로 변환했을 때 min값과 max 값을 문자열로 출력하기

input : "1 2 3 4"     
output : "1 4"

input : "-1 -2 -3 -4"
output : "-4 -1"

"""

# 나의 풀이
def solution(s):
    s_list = s.split(' ')
    s_list = [-int(s[1:]) if s[0] == "-" else int(s) for s in s_list]
    answer = ' '.join(map(str, [min(s_list), max(s_list)]))
    return answer


# 프로그래머스 풀이
def solution(s):
    s = list(map(int,s.split())) # map 함수를 사용하면 "-3"도 int로 바꿀 수 있다.
    return str(min(s)) + " " + str(max(s))
