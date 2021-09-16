"""
https://programmers.co.kr/learn/courses/30/lessons/60057

주어진 문자열을 압축하여 가장 짧은 길이를 반환하기

input	output
"aabbaccc"	7
"ababcdcdababcdcd"	9
"abcabcdede"	8
"abcabcabcabcdededededede"	14
"xababcdcdababcdcd"	17

"""

# 나의 풀이 
def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2+1):
        seq, seq_num, zipped = '', 1, ''
        for i in range(0,len(s),step):
            token = s[i:i+step]
            if seq == token:
                seq_num += 1
            else:
                _zip_add = str(seq_num)+seq if seq_num > 1 else seq 
                zipped += _zip_add
                seq_num = 1
                seq = token
        
        # 코드 중복을 줄이는 방법 찾기
        # 1. s 뒷부분에 패딩 추가하기 (계산량이 지금보다 늘어남)
        # 2. seq_num, seq를 리스트로 묶고 나중에 한번에 계산(이것도 패딩을 추가해야함)
        # for문을 적게 사용하면서 메모리는 많이 쓰지 않는 방법이 있을까?
        _zip_add = str(seq_num)+seq if seq_num > 1 else seq 
        zipped += _zip_add
                
        if len(zipped) < answer:
            answer = len(zipped)
    return answer