# 백트래킹 - N과 M
import sys
n, m = map(int, sys.stdin.readline().split())

def combination(arr, r):
    # 1.
    arr = sorted(arr)

    # 2.
    def generate(chosen):
        if len(chosen) == r:
            print(' '.join(map(str, chosen)))
            return

    	# 3.
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()
    generate([])

combination(list(range(1, n+1)), m)