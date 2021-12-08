import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    is_vps = list(input().rstrip())
    left_ = []
    right_ = []

    if is_vps[0] == "(" and is_vps[-1] == ")" and is_vps.count("(") == is_vps.count(")"):
        vps = True
        for i in range(len(is_vps)):
            if is_vps[i] == "(":
                left_.append(i)
            else:
                right_.append(i)

        for l, r in zip(left_, right_):
            if l > r:
                vps = False
                break
        if vps:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")


# stack을 쌓아서 0이면 YES, -1이면 NO
for _ in range(N):
    is_vps = list(input().rstrip())
    stack = 0
    for i in is_vps:
        if i == "(":
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                break
    if stack == 0:
        print("YES")
    else:
        print("NO")
