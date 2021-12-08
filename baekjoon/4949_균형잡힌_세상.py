import sys
input = sys.stdin.readline

while True:
    s_list = list(str(input()))[:-1]
    if s_list == ["."]:
        break
    else:
        stack = []
        unbalance = False
        for i in s_list:
            if i == "(" or i == "[":
                stack.append(i)
            elif i == ")":
                if len(stack) and stack[-1] == "(":
                    stack.pop()
                else:
                    unbalance = True
                    break
            elif i == "]":
                if len(stack) and stack[-1] == "[":
                    stack.pop()
                else:
                    unbalance = True
                    break
        if not unbalance and len(stack) == 0:
            print("yes")
        else:
            print("no")
