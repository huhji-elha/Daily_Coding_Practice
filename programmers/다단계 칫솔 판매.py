"""
https://programmers.co.kr/learn/courses/30/lessons/77486

각 판매원의 이름을 담은 배열 enroll, 
각 판매원을 다단계 조직에 참여시킨 다른 판매원의 이름을 담은 배열 referral, 
판매량 집계 데이터의 판매원 이름을 나열한 배열 seller, 
판매량 집계 데이터의 판매 수량을 나열한 배열 amount가 매개변수로 주어질 때, 
각 판매원이 득한 이익금을 나열한 배열을 return 하도록 solution 함수를 완성해주세요.

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referrel = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
"""

# 나의 풀이
# dict 여러개 써서 DFS로 풀기
def solution(enroll, referral, seller, amount):
    enroll_index, enroll_amount = {}, {}
    for i in range(len(enroll)):
        enroll_index[enroll[i]] = i
        enroll_amount[enroll[i]] = 0

    for i, s in enumerate(seller):
        sell = amount[i]*100
        enroll_amount[s] += sell - int(sell/10)
        sell = int(sell/10)
        node = referral[enroll_index[s]]
        while node != "-" and sell>0: # sell이 0이 된 상태에서 계속 while문이 돌면 시간 초과가 발생한다.
            enroll_amount[node] += sell - int(sell/10)
            node = referral[enroll_index[node]]
            sell = int(sell/10)
    return [enroll_amount[enroll[value]] for key, value in enroll_index.items()]
