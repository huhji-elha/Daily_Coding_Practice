import sys
n = int(sys.stdin.readline())

if n < 10:
    n = '0' + str(n)


def get_next_n(n: str):
    n2 = int(n[0]) + int(n[1])
    next_n = n[1] + str(n2)[-1]
    return next_n


count = 0
start = str(n)
while 1:
    next_n = get_next_n(str(n))
    count += 1
    if start == next_n:
        break
    n = next_n

print(count)
