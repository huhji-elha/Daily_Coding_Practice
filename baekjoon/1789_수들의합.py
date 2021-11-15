import sys
S = int(sys.stdin.readline())
cnt = 0
answer = 0

while True:
    cnt += 1
    answer += cnt
    if answer > S:
        cnt -= 1
        print(cnt)
        break

    """
    sum = 1+2+...+p 일때 sum > S이면 정답인 이유
    sum > S를 만족하는 S의 최대값을 S2라 할 때
    S2는 1+2+...+p-1 < sum 를 만족한다.
    
    이때 S2 + p > S이므로 S의 최대값은 S2 + p -1 이다.
    
    S2에 더해진 1부터 p-1까지의 수를 큰 수부터 1씩 증가시키면 더해진 숫자들은
    겹치지 않고 S2가 1씩 증가하여 sum을 찾을 수 있다.
    """
