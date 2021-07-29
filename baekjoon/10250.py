import math 

t = int(input())

def get_hotel_number(h, w, n):
    y = n%h
    if y == 0:
        y = h
    x = n//h
    if n/h > n//h:
        x = math.ceil(n/h)
    if len(str(x)) == 1:
        z = f"{y}0{x}"
        return int(z)
    else:
        z = f"{y}{x}"
        return int(z)

res_list = []
for i in range(t):
    h, w, n = map(int, input().split())
    res_list.append(get_hotel_number(h, w, n))

for i in range(t):
    print(res_list[i])