"""
https://programmers.co.kr/learn/courses/30/lessons/12953

배열의 최소공배수 반환하기

input       output
[2,6,8,14]	168
[1,2,3]	6
"""


# 나의 풀이 01 -- 가장 큰 수의 배수에서 나누기
arr = [1,2,3]
def solution(arr):
    i = 1
    while True:
        _arr = []
        for n in arr[:-1]:
            _arr.append(arr[-1]*i%n)
        if sum(_arr) == 0:
            return arr[-1]*i
        i+=1
print(solution(arr))

# 나의 풀이 02 -- 최대공약수로 최대공배수 구하기