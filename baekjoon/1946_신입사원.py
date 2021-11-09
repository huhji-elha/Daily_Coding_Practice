import sys
n = int(sys.stdin.readline())


def new_recruits():
    N = int(sys.stdin.readline())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, sys.stdin.readline().split())))

    arr.sort()
    answer = 0
    m = arr[0][1]
    for i in range(len(arr)):
        if i == 0:
            answer += 1
        else:
            if arr[i][1] < m:
                m = arr[i][1]
                answer += 1

    return answer


for _ in range(n):
    print(new_recruits())
