a, b, v = map(int, input().split())
i = (v-a)//(a-b)
h = i*(a-b)
while True:
    i += 1
    h += a
    if h >= v:
        print(i)
        break
    h -= b