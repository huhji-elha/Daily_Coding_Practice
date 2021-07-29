n = int(input())

i = 2
while i <= n:
    if n%i == 0:
        print(i)
        n = n//i
        if n//i == 1:
            print(n)
            break
    else:
        i += 1
