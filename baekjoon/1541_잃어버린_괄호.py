import sys
n = str(sys.stdin.readline())
n = n.replace('\n', '')
n_list = n.split('-')

for i in range(len(n_list)):
    m = sum(list(map(int, n_list[i].split('+'))))
    n_list[i] = m

answer = n_list[0]
for n in n_list[1:]:
    answer -= n

print(answer)
