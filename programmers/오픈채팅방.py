"""
https://programmers.co.kr/learn/courses/30/lessons/42888

record
["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]	

result
["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
"""

def solution(record):
    name_dict = {}
    answer = []
    answer_print = {"Enter":"님이 들어왔습니다.", "Leave":"님이 나갔습니다."}
    
    for rec in record:
        rec_list = rec.split()
        if rec_list[0] != "Leave":
            name_dict[rec_list[1]] = rec_list[2]

    for rec in record:
        r = rec.split()
        if r[0] != "Change":
            answer.append(f"{name_dict[r[1]]}{answer_print[r[0]]}")
        
    return answer