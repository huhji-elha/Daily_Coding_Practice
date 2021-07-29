a, b, c = map(int,input().split())
if b >= c:
    print(-1)
elif c-b > 0:
    i = a//(c-b)
    print(i+1)