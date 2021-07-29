import sys 
from collections import defaultdict
a_square = defaultdict(int)
b_square = defaultdict(int)
for i in range(3):
    a, b = map(int, sys.stdin.readline().split())
    a_square[a] += 1
    b_square[b] += 1


print([k for k,v in a_square.items() if v == 1][0])
print([k for k,v in b_square.items() if v == 1][0])