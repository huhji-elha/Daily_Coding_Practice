import sys 
t = int(sys.stdin.readline())

def Turret(arr):
    x1, y1, r1, x2, y2, r2 = arr 
    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    
    if d:
        if r1 + r2 == d:
            return 1
        elif abs(r1 - r2) == d:
            return 1
        elif abs(r1 - r2) > d:
            return 0
        elif r1 + r2 > d:
            return 2
        elif r1 + r2 < d:
            return 0
        else:
            return 0
    else:
        if r1 == r2:
            return -1
        else:
            return 0

for i in range(t):
    arr = list(map(int, sys.stdin.readline().split()))
    res = Turret(arr)
    print(res)