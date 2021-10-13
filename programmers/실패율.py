"""
https://programmers.co.kr/learn/courses/30/lessons/42889

실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

N	stages	result
5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
4	[4,4,4,4,4]	[4,1,2,3]

"""
import collections 
def solution(N, stages):
    s = dict(collections.Counter(stages))
    stages_set = set(stages)
    not_clear = 0
    stage_dict = dict()

    for i in range(1, N+1):
        if i in stages_set:
            stage_dict[i] = s[i]/(len(stages) - not_clear)
            not_clear += s[i]
        else:
            stage_dict[i] = 0
    return dict(sorted(stage_dict.items(), key=(lambda x:x[1]), reverse=True)).keys()