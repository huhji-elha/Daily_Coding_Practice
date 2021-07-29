# 팩토리얼
import sys
n = int(sys.stdin.readline())
i = 1
f = 1
def factorial(i, n):
    global f
    if i == n:
        return
    elif n == 0:
        return
    i += 1
    f *= i
    factorial(i, n)
    
factorial(i, n)
print(f)