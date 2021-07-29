# 백트래킹 - N과 M
# 중복 있는 조합 

import sys 
n, m = map(int, sys.stdin.readline().split())

def combination2(m, chosen, arr):
    if len(chosen) == m:
        print(' '.join(map(str, chosen)))
        return 
    else:
        for i in range(len(arr)):
            chosen.append(arr[i])
            combination2(m, chosen, arr[i:])
            chosen.pop()
combination2(m, [], list(range(1,n+1)))
            