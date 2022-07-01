#https://programmers.co.kr/learn/courses/30/lessons/92334
#신고 결과 받기
#DICTIONARY를 적극적으로 활용하자

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    rpter = {}
    rpted = {}
    
    report = set(report)
    
    for r in report:
        #신고 받은 횟수 정리
        if r.split()[1] not in rpted:
            rpted[r.split()[1]] = 1
        else:
            rpted[r.split()[1]] += 1
        
        #신고 한 대상 정리
        if r.split()[0] not in rpter:
            rpter[r.split()[0]] = [r.split()[1]]
        else:
            rpter[r.split()[0]] += [r.split()[1]]
    
    for a, b in rpted.items():
        if b >= k:
            #print(a, "Over")
            for usr, check in rpter.items():
                if a in check:
                    #print(usr, b)
                    #index(값) -> 배열에서의 index를 반환
                    answer[id_list.index(usr)] += 1
    
    #print(rpter)
    #print(rpted)
    return answer