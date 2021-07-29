# 재귀함수 - 하노이의 탑
import sys

N = int(sys.stdin.readline())
hanoi_list = []
def hanoi(n, from_pos, to_pos, aux_pos):
    global hanoi_list
    if n == 1:
        hanoi_list.append(f"{from_pos} {to_pos}")
        return
    hanoi(n-1, from_pos, aux_pos, to_pos) # n-1개를 보조기둥으로 전부 옮긴 후에 
    hanoi_list.append(f"{from_pos} {to_pos}") # from_pos에 있는 가장 큰 원반을 to_pos로 옮김
    hanoi(n-1, aux_pos, to_pos, from_pos) # 보조기둥에 있는 n-1개 원반을 to_pos로 옮김 
    
hanoi(N, 1, 3, 2)
print(len(hanoi_list))
for i in hanoi_list:
    print(i)