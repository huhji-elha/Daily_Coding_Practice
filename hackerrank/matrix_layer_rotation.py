"""
https://www.hackerrank.com/challenges/matrix-rotation-algo/problem?isFullScreen=false

m x n 매트릭스를 r 횟수만큼 반시계방향으로 회전하기.

STDIN        Function
-----        --------
4 4 2        rows m = 4, columns n = 4, rotation factor r = 2
1 2 3 4      matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
5 6 7 8
9 10 11 12
13 14 15 16
"""
# 아이디어01 : 이중 배열 순환하기
# 아이디어02 : 내부 배열은 항상 순환할 수 있다. min(m, n)%2 = 0

#!/bin/python3


def matrixRotation(matrix, r):
    def rotateLayer(x1, y1, x2, y2, r):
        idx01, idx02, idx03, idx04 = [], [], [], []
        for i in range(y1, y2):
            idx01.append((x1, i))
            idx03.append((x2-1, i))

        for i in range(x1, x2):
            idx02.append((i, y2-1))
            idx04.append((i, x1))
        idx_list = idx01[:-1] + idx02[:-1] + \
            idx03[::-1][:-1] + idx04[::-1][:-1]

        layer = [matrix[i][j] for i, j in idx_list]
        r = r % len(layer) if r > len(layer) else r
        extra = layer[:r]
        layer2 = layer[r:] + extra

        for i in range(len(idx_list)):
            x, y = idx_list[i]
            matrix[x][y] = layer2[i]

    x2 = len(matrix)
    y2 = len(matrix[0])
    x1, y1 = 0, 0
    while x2 > x1 and y2 > y1:
        rotateLayer(x1, y1, x2, y2, r)
        x1 += 1
        y1 += 1
        x2 -= 1
        y2 -= 1

    # hackerrank에서 출력시
    for row in matrix:
        for m in row:
            print(m, end=" ")
        print()


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
