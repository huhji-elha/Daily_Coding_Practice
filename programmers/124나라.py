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

# 첫번째 풀이
# 가장 근사한 값을 찾아 해당 범위 내에 있는 조합을 구하기
# 답은 맞으나 효율성이 떨어짐.
import math
def _product(*args, repeat=1, stop):
    pools = [tuple(pool) for pool in args] * repeat
    i, result = 0, [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        if i == stop:
            yield tuple(prod)
        i += 1

def solution(n):
    t = math.log((2/3*n+1),3) # 등비수열의 합 공식 사용
    _arr_count = math.ceil(t)
    _arr_num = 0
    for i in range(1, _arr_count):
        _arr_num += 3**i
    _stop = 0 if n == _arr_num else n - _arr_num -1
    pr = _product(*["124"], repeat=_arr_count, stop=_stop)
    return ''.join(list(pr)[0])


# 두번째 풀이
# 3진법을 활용하기

def solution(n):
    ll = []
    while True:
        if n//3 > 0:
            if n%3 == 0:
                ll.append(3)
                n = n//3 - 1
            else:
                ll.append(n%3)
                n = n//3
        else:
            if n > 0: ll.append(n)
            break
    return ''.join(map(str, ll[::-1])).replace('3','4')

# 프로그래머스 풀이
# 3진법을 더 간단하게 풀이하기

def solution(n):
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3
    return answer 