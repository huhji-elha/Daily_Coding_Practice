import sys
input = sys.stdin.readline

while True:
    N = input().rstrip()
    if N == "0":
        break
    N_list = list(map(str, list(N)))
    if N_list == N_list[::-1]:
        print("yes")
    else:
        print("no")
