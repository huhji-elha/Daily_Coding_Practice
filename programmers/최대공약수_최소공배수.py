"""
두 수의 최대공약수와 최소공배수 반환하기
"""

def solution(n, m):
    for i in range(min(n,m), 1, -1):
        if n%i == 0 and m%i == 0:
            gcd = i
            break
    return [gcd, m*n//gcd]

print(solution(10,12))