import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
que = deque([])
for _ in range(N):
    command = input().rstrip()
    if command.startswith("push"):
        x = int(command.split(" ")[-1])
        que.append(x)
    elif command.startswith("pop"):
        if len(que):
            print(que.popleft())
        else:
            print(-1)
    elif command.startswith("size"):
        print(len(que))
    elif command.startswith("empty"):
        if len(que):
            print(0)
        else:
            print(1)
    elif command.startswith("front"):
        if len(que):
            print(que[0])
        else:
            print(-1)
    else:
        if len(que):
            print(que[-1])
        else:
            print(-1)
