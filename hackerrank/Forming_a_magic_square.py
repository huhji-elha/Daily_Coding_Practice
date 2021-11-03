"""
https://www.hackerrank.com/challenges/magic-square-forming/problem?isFullScreen=false

주어진 행렬을 마방진 행렬로 수정할 때 최소 cost를 구하기

Input
4 9 2
3 5 7
8 1 5

Output
1

"""

# 아이디어01 : 3x3 마방진 행렬의 경우의 수를 모두 구하여 주어진 행렬과 차이 구하기
# 아이디어02 : 3x3 마방진 행렬을 하나 구한 뒤 행렬을 회전, 반전 시켜가며 가능한 경우의 마방진 행렬을 구하기
import os


def formingMagicSquare(s):
    arr = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]  # 기본 마방진 행렬
    answer = []
    flatten_s = sum(s, [])  # 이중 배열 풀기

    def rotate(arr):  # 이중 배열 90도 회전
        r_arr = [[0] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                r_arr[j][3-i-1] = arr[i][j]
        return r_arr

    def get_cost(arr, s):  # 두 배열의 차이 구하기
        return sum([abs(arr[x]-s[x]) for x in range(len(arr))])

    for _ in range(4):  # 하나의 마방진 행렬에 대해 4번 회전할 때 각각 반전 행렬 구하기
        answer.append(get_cost(sum(arr, []), flatten_s))
        arr2 = list(map(list, zip(*arr)))
        answer.append(get_cost(sum(arr2, []), flatten_s))
        arr = rotate(arr)

    return min(answer)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
