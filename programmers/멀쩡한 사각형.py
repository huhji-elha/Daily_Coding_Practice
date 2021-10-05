"""
https://programmers.co.kr/learn/courses/30/lessons/62048

가로의 길이 W와 세로의 길이 H가 주어질 때, 사용할 수 있는 정사각형의 개수를 구하는 solution 함수를 완성해 주세요.

W	H	result
8	12	80
"""

# 첫번째 풀이
# 답은 맞으나 시간초과 발생
import math
def solution(w,h):
    return sum(map(lambda x:math.floor(-h/w*x+h), range(1,w)))*2

# 두번째 풀이
# 빠르게 풀 수 있는 경우에는 바로 답을 리턴하도록
def solution(w,h):
    if w == 1 or h == 1: 
        return 0
    if w == h: 
        return w*h - w
    else:
        return sum(map(lambda x:int(-h/w*x+h), range(1,w)))*2
    
# 세번째 풀이
# 최대공약수 사용하기
def gcd(a,b): return b if (a==0) else gcd(b%a,a)    
def solution(w,h): return w*h-w-h+gcd(w,h)