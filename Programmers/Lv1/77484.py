#https://programmers.co.kr/learn/courses/30/lessons/77484?language=python3
#로또의 최고 순위와 최저 순위
#간단화의 간단화.

def solution(lottos, win_nums):
    answer = [0, 0]
    
    MAX = 1
    MIN = 6
    lottos.sort(reverse = True)
    Correct = 0
    win_nums.sort(reverse = True)
    Possibility = 0
    
    #print(lottos)
    #print(win_nums)
    
    for i in range(6):
        if lottos[i] == 0:
                Possibility += 1
        else:
            for j in range(6):
                if lottos[i] == win_nums[j]:
                    Correct += 1
    
    if 7 - Correct < 6:
        answer[1] = 7 - Correct
    else:
        answer[1] = 6
        
    if 7 - (Correct + Possibility) < 6:
        answer[0] = 7 - (Correct + Possibility)
    else:
        answer[0] = 6
    
    return answer