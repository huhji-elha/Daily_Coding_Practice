import sys
T = int(sys.stdin.readline())

# 첫번째 풀이 -- 시간 초과
# def fibo(x, c0, c1):
#     if x == 0:
#         return 0, c0+1, c1
#     elif x == 1:
#         return 1, c0, c1+1
#     x_1 = fibo(x-1, c0, c1)
#     x_2 = fibo(x-2, c0, c1)
#     d[x] = x_1[0] + x_2[0]
#     c0 = x_1[1] + x_2[1]
#     c1 = x_1[2] + x_2[2]
#     return d[x], c0, c1


# for _ in range(T):
#     N = int(sys.stdin.readline())

#     d = [0]*(N+1)
#     c0 = 0
#     c1 = 0

#     _, c0, c1 = fibo(N, c0, c1)
#     print(c0, c1, sep=" ")

# 두번째 풀이 -- f(0)과 f(1) 수열을 구하는 함수 작성
def get_0_num(x):
    d = [0]*(41)
    d[0] = 1
    d[1] = 0
    d[2] = 1
    d[3] = 1
    for i in range(4, x+1):
        d[i] = d[i-1] + d[i-2]
    return d[x]


def get_1_num(x):
    d = [0]*(41)
    d[0] = 0
    d[1] = 1
    d[2] = 1
    for i in range(3, x+1):
        d[i] = d[i-1] + d[i-2]
    return d[x]


for _ in range(T):
    N = int(sys.stdin.readline())
    print(get_0_num(N), get_1_num(N), sep=" ")
