import sys
n = 1000 - int(sys.stdin.readline())
m_list = [500, 100, 50, 10, 5, 1]
answer = 0
for coin in m_list:
    answer += n//coin
    n = n % coin

print(answer)
