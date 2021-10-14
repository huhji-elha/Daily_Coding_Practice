"""
https://programmers.co.kr/learn/courses/30/lessons/43165

사용할 수 있는 숫자가 담긴 배열 numbers, 
타겟 넘버 target이 매개변수로 주어질 때 
숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

numbers = [1,1,1,1,1]
target = 3

"""

# 나의 풀이
# 너비 우선 탐색으로 풀기
# 메모리를 과하게 사용하는 문제가 있다.
def solution(numbers, target):
    first_node = numbers.pop()
    target_list, target_list2 = [first_node, -first_node], []
    while len(numbers) > 0:
        node = numbers.pop()
        for t in target_list:
            target_list2.append(t+node)
            target_list2.append(t-node)
        target_list, target_list2 = target_list2, []
    return target_list.count(target)

# 프로그래머스 풀이
# 재귀함수로 풀기
def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])