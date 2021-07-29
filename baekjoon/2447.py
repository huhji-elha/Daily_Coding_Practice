# 재귀 패턴으로 별 찍기
import sys
N = int(sys.stdin.readline())

star_list =[['*','*','*'],
            ['*', ' ', '*'],
            ['*', '*', '*']]
res = []

def draw_star(n, star_list):
    global N, res
    new_list = []
    
    for i in range(n):
        if i in range(n//3, n-(n//3)):
            new_list.append(star_list[i%(n//3)]+[' ']*(n//3)+star_list[i%(n//3)])
        else:
            new_list.append(star_list[i%(n//3)]*3)
    if n == N:
        res = new_list
        return
    else:
        n *= 3
        draw_star(n, new_list)
    
if N == 3:
    res = star_list
else:
    draw_star(9, star_list)

for l in res:
    print(''.join(l))
