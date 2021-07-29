import sys 
x, y, w, h = map(int, sys.stdin.readline().split())

_distance = [w-x, h-y, x, y]
print(min(_distance))