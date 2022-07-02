#https://programmers.co.kr/learn/courses/30/lessons/92341#
#주차 요금 계산
#미완성. 43.8%

import math

def solution(fees, records):
    answer = []
    parking = {}
    total_time = {}
    
    for r in records:
        car = int(r.split()[1])
        if r.split()[2] == 'IN':
            time = list(map(int, r.split()[0].split(":")))
            parking[car] = time[0] * 60 + time[1]
            if car not in total_time:
                total_time[car] = 0
            #print(parking)
        elif r.split()[2] == 'OUT':
            #print("parking?...", parking)
            time = list(map(int, r.split()[0].split(":")))
            total_time[car] += (time[0] * 60 + time[1] - parking[car])
            del parking[car]
            #print(r.split()[1], "total times: ", total_time)
    
    total_time = sorted(total_time.items())
    print(total_time)
    print(parking)
    #print(len(total_time))
    #print(len(parking))
    
    for c, t in total_time:
        if c in parking:
            #print(c)
            t += 23 * 60 + 59 - parking[c]
        if t < fees[0]:
            answer.append(5000)
        else:
            answer.append(fees[1] + math.ceil((t - fees[0]) / fees[2]) * fees[3])
        print(c, t)
    
    return answer