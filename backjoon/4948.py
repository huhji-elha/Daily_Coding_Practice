def get_prime(m, n):
    sieve = [True]*(n+1)
    sieve[:2] = [False]*2
    for i in range(2, int(n**0.5)+1):
        if sieve[i] == True:
            for j in range(i+i, n+1, i):
                sieve[j] = False
    return sum(sieve[m+1:])

while True:
    n = int(input())
    if n == 0:
        break
    print(get_prime(n, 2*n))