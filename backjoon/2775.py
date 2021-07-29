t = int(input())

def get_a_b(k, n):
    l = list(range(1, n+1))
    l_k= []
    kk = 0

    while True:
        if kk == k:
            break
        for j in range(1, n+1):
            l_k.append(sum(l[:j]))
        kk += 1
        l, l_k = l_k, []
    return l[-1]

res_list = []
for i in range(t):
    k = int(input())
    n = int(input())
    res_list.append(get_a_b(k, n))

for i in range(t):
    print(res_list[i])