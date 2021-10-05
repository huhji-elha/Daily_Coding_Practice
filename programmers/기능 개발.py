"""
https://programmers.co.kr/learn/courses/30/lessons/42586

progresses	speeds	return
[93, 30, 55]	[1, 30, 5]	[2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
"""

# 나의 풀이 
def get_progress(progresses, speeds):
    _progress = []
    for p, s in zip(progresses, speeds):
        _progress.append(p+s)
    return _progress

def get_finish(progress):
    for i in range(len(progress)):
        if progress[i] < 100:
            return i
    return len(progress)

def solution(progresses, speeds):
    answer = []
    while len(progresses) > 0:
        progresses = get_progress(progresses, speeds)
        if progresses[0] > 99:
            _idx = get_finish(progresses)
            progresses = progresses[_idx:]
            speeds = speeds[_idx:]
            answer.append(_idx)
        if len(progresses) == 0:
            break
    return answer

# 더 좋은 풀이 방법
# 100에 도달할 때까지 며칠이 필요한지 구하고 계단식으로 자르기
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        print((p-100)//s)
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]