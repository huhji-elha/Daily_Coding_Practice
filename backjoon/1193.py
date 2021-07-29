k = int(input())
i, n = 1, 1
while True:
    if k <= n:
        nn = n - k
        if i%2 == 0:
            print(f"{i-nn}/{1+nn}")
            break
        else:
            print(f"{1+nn}/{i-nn}")
            break
    i += 1
    n += i