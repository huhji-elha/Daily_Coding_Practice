# 피보나치 수
import sys 
n = int(sys.stdin.readline())
p_list = [0, 1]
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for i in range(2, n+1):
        p_list.append(sum(p_list[i-2:]))
    print(p_list[-1])
            
            