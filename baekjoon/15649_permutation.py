# 백트래킹 - N과 M 01
import sys 
n, m = map(int, sys.stdin.readline().split())

def permutation(arr, m):
    used = [0 for _ in range(len(arr))]
    
    def generate(res_list, used):
        if len(res_list) == m:
            print(' '.join(map(str,res_list)))
            return 
        
        for i in range(len(arr)):
            if not used[i]:
                res_list.append(arr[i])
                used[i] = 1
                generate(res_list, used)
                used[i] = 0
                res_list.pop()
                
    generate([], used)

permutation(list(range(1, n+1)), m)

