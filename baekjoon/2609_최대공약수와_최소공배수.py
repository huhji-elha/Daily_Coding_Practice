import sys
a, b = list(map(int, sys.stdin.readline().split()))

# 최대공약수 : 유클리드 호재법
A = max(a, b)
B = min(a, b)


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


ab_gcd = gcd(A, B)
print(ab_gcd)
print((A*B)//ab_gcd)  # 최소공배수 : 두 수의 곱에서 최대공약수를 나눈 것.
