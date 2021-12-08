import sys
import string
input = sys.stdin.readline
L = int(input())
s = list(input().rstrip())
alpha_dict = {alphabet: i for alphabet, i in zip(
    list(string.ascii_lowercase), range(1, 27))}

res = 0
for i in range(L):
    res += alpha_dict[s[i]] * (31**i)

print(res % 1234567891)
