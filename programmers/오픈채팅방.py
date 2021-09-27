"""
https://programmers.co.kr/learn/courses/30/lessons/42888

record
["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]	

result
["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
"""

def solution(record):
    name_dict = {}
    enter_list = []
    answer = []
    for rec in record:
        rec_list = rec.split()
        if rec_list[0] != "Leave":
            name_dict[rec_list[1]] = rec_list[2]
        if rec_list[0] != "Change":
            enter_list.append([rec_list[0], rec_list[1]])

    for ent in enter_list:
        if ent[0] == "Enter":
            answer.append(f"{name_dict[ent[1]]}님이 들어왔습니다.")
        else:
            answer.append(f"{name_dict[ent[1]]}님이 나갔습니다.")
        
    return answer