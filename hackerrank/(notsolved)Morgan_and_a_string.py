"""
https://www.hackerrank.com/challenges/morgan-and-a-string/problem?isFullScreen=false

문자열 stack에서 알파벳을 순서대로 하나씩 꺼내기

input:
2
JACK
DANIEL
ABACABA
ABACABA

output:
DAJACKNIEL
AABABACABACABA
"""

# 아이디어 01: deque를 사용해서 앞선 순서의 알파벳 꺼내기
# 아이디어 02: 같은 알파벳일 경우 뒤의 알파벳까지 비교하기

import sys
from collections import deque

# Test Case는 맞으나 Time Exceeded인 상태
def morganAndString(a, b):
    def check_priority(a_deque, b_deque):
        i = 0
        _a = a_deque[i]
        _b = b_deque[i]
        while i < max(len(a_deque), len(b_deque)):
            if _a == _b:
                i += 1
                _a = a_deque[min(i, len(a_deque)-1)]
                _b = b_deque[min(i, len(b_deque)-1)]
            elif _a > _b:
                return 0
            else:
                return 1

    a_deque = deque(a)
    b_deque = deque(b)

    result = ''
    while a_deque and b_deque:
        if a_deque[0] == b_deque[0]:
            if check_priority(a_deque, b_deque):
                result += a_deque.popleft()
            else:
                result += b_deque.popleft()
        elif a_deque[0] > b_deque[0]:
            result += b_deque.popleft()
        else:
            result += a_deque.popleft()

    result += ''.join(a_deque+b_deque)
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['sample.txt'], 'w')

    t = int(sys.stdin.readline())

    for t_itr in range(t):
        a = str(sys.stdin.readline()).replace('\n', '')

        b = str(sys.stdin.readline()).replace('\n', '')

        result = morganAndString(a, b)
        print(result)

        # fptr.write(result + '\n')

    # fptr.close()
