import sys
input = sys.stdin.readline
i = 1
while True:
    L, P, V = list(map(int, input().split()))
    if L == 0 and P == 0 and V == 0:
        break

    share = V//P
    if V % P > L:
        remainder = L
    else:
        remainder = V % P
    res = share*L + remainder
    print(f"Case {i}: {res}")
    i += 1
