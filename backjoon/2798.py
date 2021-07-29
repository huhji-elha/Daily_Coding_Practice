# blackjack
import sys 
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort(reverse=True)

def black_jack(M, arr):
    _max = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                card_sum = arr[i] + arr[j] + arr[k]
                if card_sum <= M and card_sum > _max:
                    _max = card_sum
    return _max 
                
print(black_jack(M, arr))