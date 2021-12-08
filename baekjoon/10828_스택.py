import sys
input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N):
    command = input().rstrip()
    if command.startswith("push"):
        x = int(command.split(" ")[-1])
        stack.append(x)
    elif command.startswith("pop"):
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif command.startswith("size"):
        print(len(stack))
    elif command.startswith("empty"):
        if len(stack):
            print(0)
        else:
            print(1)
    else:
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
