"""
10진법 수를 124 나라의 규칙대로 나타내기...

10진법	124 나라
1	        1	
2	        2	
3	        4	
4	        11
5	        12	
6       	14
7	        21
8	        22
9	        24
10	        41

42
44
111

n은 500,000,000이하의 자연수

"""

def solution(n):
    _124 = {"1", "2", "4"}
    i = 0
    num = 0
    while True:
        if set(str(num)) < _124:
            i += 1
        if i == n:
            return num
        num += 1

print(solution(10))