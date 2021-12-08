import sys
from collections import deque
input = sys.stdin.readline
N = int(input())

deq = deque([])
for _ in range(N):
    command = input().rstrip()
    if command.startswith("push_front"):
        x = int(command.split(" ")[-1])
        deq.appendleft(x)
    elif command.startswith("push_back"):
        x = int(command.split(" ")[-1])
        deq.append(x)
    elif command.startswith("pop_front"):
        if len(deq):
            print(deq.popleft())
        else:
            print(-1)
    elif command.startswith("pop_back"):
        if len(deq):
            print(deq.pop())
        else:
            print(-1)
    elif command.startswith("size"):
        print(len(deq))
    elif command.startswith("empty"):
        if len(deq):
            print(0)
        else:
            print(1)
    elif command.startswith("front"):
        if len(deq):
            print(deq[0])
        else:
            print(-1)
    else:
        if len(deq):
            print(deq[-1])
        else:
            print(-1)
