t = int(input())
arr = list(map(int, input().split()))

def get_prime_num(arr):
    prime_num = 0
    for p in arr:
        if p < 2:
            continue
        nn = 0
        for i in range(2, int(p**0.5)+1):
            if p%i == 0:
                nn += 1
                break
        if nn == 0:
            prime_num += 1
    return prime_num

print(get_prime_num(arr))