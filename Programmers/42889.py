#https://programmers.co.kr/learn/courses/30/lessons/42889
#실패율
#테스트 케이스 22번 때문에 고생함. 대상자 계산을 간결히 함.

def solution(N, stages):
    answer = [0] * N
    usr_in_stages = {}
    target = {}
    failure = {}
    clear = len(stages)
    
    #정답. 전판까지 클리어한 사람(대상자) 계산을 단순 뺄셈으로 구현
    for i in range(1, N + 1):
        if clear != 0:
            count = stages.count(i)
            failure[i] = count / clear
            clear -= count
        else:
            failure[i] = 0
    
    #print(failure)
    sorted_failure = sorted(failure.items(), key = lambda item: item[1], reverse = True)
    for i in range(N):
        answer[i] = sorted_failure[i][0]
    
    #테스트케이스 22번 시간 초과 답안. 대상자를 각각 구할 필요가 없었음.
    '''for s in sorted(stages):
        if s not in usr_in_stages:
            usr_in_stages[s] = 1
        else:
            usr_in_stages[s] += 1
        
        for i in range(1, N + 1):
            if s >= i:
                if i not in target:
                    target[i] = 1
                else:
                    target[i] += 1
    
    for s, t in target.items():
        if s not in usr_in_stages or target[s] == 0:
            failure[s] = 0
        else:
            failure[s] = usr_in_stages[s] / target[s]
    
    sorted_failure = sorted(failure.items(), key = lambda item: item[1], reverse = True)
    #print(sorted_failure)
    if len(sorted_failure) < N:
        for i in range(len(sorted_failure), N):
            sorted_failure.append((i + 1, 0))
                                  
    for i in range(N):
        answer[i] = sorted_failure[i][0]'''
    
    return answer