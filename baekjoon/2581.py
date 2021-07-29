def get_prime(m, n):
    sieve = [True]*(n+1)
    if m < 2:
        sieve[m:2] = [False]*len(sieve[m:2])
    for i in range(2, int(n**0.5)+1):
        if sieve[i] == True:
            if i > m:
                s = (i - m)+i
            elif m%i == 0 and m//i > 1:
                s = 0
            else:
                s = (m // i)*i + i - m
            for j in range(s+m, n+1, i):
                if sieve[j] == True:
                    sieve[j] = False
                
    return [i for i in range(m, n+1) if sieve[i] == True]

m = int(input())
n = int(input())

arr = get_prime(m, n)
print(f"{sum(arr)}\n{arr[0]}" if arr else -1)
