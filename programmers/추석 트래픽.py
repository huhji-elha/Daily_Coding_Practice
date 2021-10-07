"""
https://programmers.co.kr/learn/courses/30/lessons/17676

주어진 log에서 각 프로세스들의 초당 최대 처리량 구하기

입력: [
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]

출력: 1
"""

# 나의 풀이
# 시작 시간과 작업 완료 시간을 각각 datetime으로 구한 뒤 
# 각 프로세스의 완료시간 + 1초 - 0.001초 이내에 시작된 프로세스 개수 구하기
from datetime import datetime, timedelta
def solution(lines):
    start, end = [], []
    for line in lines:
        t = line.split()
        start.append((datetime.strptime(t[1], "%H:%M:%S.%f") - timedelta(seconds = float(t[2][:-1])) + timedelta(seconds = 0.001)))
        end.append(datetime.strptime(t[1], "%H:%M:%S.%f"))

    max_process = 1
    for i, e in enumerate(end[:-1]):
        end_1 = e + timedelta(seconds=1) - timedelta(seconds=0.001)
        m = 1
        for s in start[i+1:]:
            if end_1 >= s: # 프로세스 완료시간이 오름차순으로 정렬되어 있으므로 시작시간이 이내인 프로세스만 구하면 된다.
                m += 1
        max_process = m if m > max_process else max_process
    return max_process