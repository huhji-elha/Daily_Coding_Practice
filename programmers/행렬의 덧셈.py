"""
행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 
서로 더한 결과 리턴하기

arr1	           arr2	          return
[[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
[[1],[2]]	[[3],[4]]	[[4],[6]]

"""

def solution(arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        answer.append([a[i]+b[i] for i in range(len(a))])
    return answer

arr1=[[1],[2]]
arr2=[[3],[4]]
print(solution(arr1, arr2))