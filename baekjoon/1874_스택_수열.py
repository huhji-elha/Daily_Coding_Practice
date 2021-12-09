import sys
input = sys.stdin.readline
N = int(input())
stack_1 = [1]
stack_2 = []
target_list = []
res = ['+']
for _ in range(N):
    target_list.append(int(input()))

target_idx = 0
i = 2
flag = False
while len(stack_2) < N:
    if not len(stack_1) or stack_1[-1] < target_list[target_idx]:
        stack_1.append(i)
        i += 1
        res.append("+")
    elif stack_1[-1] == target_list[target_idx]:
        n = stack_1.pop()
        res.append("-")
        stack_2.append(n)
        target_idx += 1
    else:
        flag = True
        break

if flag:
    print("NO")
else:
    for r in res:
        print(r)
