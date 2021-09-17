"""
두 행렬 arr1과 arr2를 곱한 결과를 출력하기

arr1	                           arr2	                  return
[[1, 4], [3, 2], [4, 1]]	[[3, 3], [3, 3]]	[[15, 15], [15, 15], [15, 15]]
[[2, 3, 2], [4, 2, 4], [3, 1, 4]]	[[5, 4, 3], [2, 4, 1], [3, 1, 1]]	[[22, 22, 11], [36, 28, 18], [29, 20, 14]]
"""

# 나의 풀이
def solution(arr1, arr2):
    arr2 = list(map(list, zip(*arr2)))
    answer = []
    for first_arr in arr1:
        first_list = []
        for second_arr in arr2:
            s = sum(a*b for a,b in zip(first_arr, second_arr)) # sum 안에 zip을 넣을 수 있음...!
            # s = 0
            # for i in range(len(second_arr)):
                # s+=first_arr[i]*second_arr[i]
            first_list.append(s)
        answer.append(first_list)
    return answer

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]	
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution(arr1, arr2))

# 프로그래머스 풀이
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

# for A_row in A:
#     for B_col in zip(*B):
#         for a,b in zip(A_row, B_col)