# 정렬 - 단어 정렬
import sys
n = int(sys.stdin.readline())
word_dict = {}
for _ in range(n):
    w = str(sys.stdin.readline()).replace('\n','')
    word_dict[w] = len(w)

word_dict = sorted(word_dict.items(), key = lambda x:(x[1],x[0]))
for l in word_dict:
    print(l[0])