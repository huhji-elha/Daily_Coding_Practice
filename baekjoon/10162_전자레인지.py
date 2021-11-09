import sys
N = int(sys.stdin.readline())
time_list = [300, 60, 10]


def microwave(N):
    button = []
    for t in time_list:
        button.append(N//t)
        N = N % t

    if N:
        return [-1]
    return button


answer = microwave(N)
for a in answer:
    print(a, end=' ')
