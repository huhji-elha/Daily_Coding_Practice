"""
https://programmers.co.kr/learn/courses/30/lessons/12977

주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하기

nums	result
[1,2,3,4]	1
[1,2,7,6,4]	4
"""

# 나의 풀이
# yield 제너레이터를 사용하여 조합 직접 구현하기

def combination(array, num):
    for i in range(len(array)):
        if num == 1:
            yield [array[i]]
        else:
            for next in combination(array[i+1:], num-1):
                yield [array[i]] + next

def is_prime(num):
    for n in range(2, num//2+1):
        if num%n == 0:
            return 0
    return 1

def solution(nums):
    answer = 0
    _comb_list = list(combination(nums, 3))
    for comb in _comb_list:
        if is_prime(sum(comb)):
            answer += 1
    return answer