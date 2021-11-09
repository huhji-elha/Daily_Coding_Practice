import sys
N = int(sys.stdin.readline())


def sugar_delivery(N):
    answer = 0
    n = N // 5
    for i in range(n, -1, -1):
        if (N - i*5) % 3 == 0:
            answer = i + (N - i*5)//3
            break
    if not answer:
        return -1
    return answer


print(sugar_delivery(N))
