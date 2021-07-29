import sys
t = int(input())

m = 10000
sieve = [False]*2 + [True]*(m-1)
for i in range(2, int(m**0.5)+1):
    if sieve[i]:
        for j in range(i+i, m+1, i):
            sieve[j] = False

def get_gold_partition(n, sieve):
    _partition = {}
    for p in range(int(n/2)+1):
        if sieve[p] and sieve[n - p] and n-p-p >= 0:
            _partition[n-p-p] = (p, n-p)
    return min(_partition.items())[1]

for i in range(t):
    n = int(sys.stdin.readline())
    arr = get_gold_partition(n, sieve)
    print(f"{arr[0]} {arr[1]}")