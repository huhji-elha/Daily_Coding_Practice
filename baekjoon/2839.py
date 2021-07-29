n = int(input())

res = 9999
for i in range(n//5, -1, -1):
    if (n-(5*i))%3 == 0:
        r = i + (n-(5*i))//3
        if r < res:
            res = r
if res == 9999:
    print(-1)
else:
    print(res)