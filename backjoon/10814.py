# 정렬 - 나이순 정렬
import sys
n = int(sys.stdin.readline())
user_dict = {}
for i in range(n):
    l = list(sys.stdin.readline().split())
    l[0] = int(l[0])
    user_dict[i] = l
user_dict = sorted(user_dict.items(), key=lambda x:(x[1][0], x[0]))

for u in user_dict:
    print(' '.join(map(str, u[1])))