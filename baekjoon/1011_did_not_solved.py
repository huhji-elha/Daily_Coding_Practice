import math
t = int(input())

def FlyMeToTheAlpha(x, y):
    if y-x < 2:
        return 1
    n = math.floor(math.sqrt(2*((y-x)//2-1)))
    if n == 0:
        n = 1
    elif sum(range(1,n+1)) > (y-x)/2:
        n = n-1

    step = n
    x = x+sum(range(1,n+1))
    y = y-sum(range(1,n+1))
    i = n*2

    if y-x == 0:
        return i
    elif y-x in [step-1, step, step+1]:
        return i + 1
    else:
        return i + 2

res_list = []
for i in range(t):
    x, y = map(int, input().split())
    res_list.append(FlyMeToTheAlpha(x, y))

for i in range(t):
    print(res_list[i])