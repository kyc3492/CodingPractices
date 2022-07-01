#https://programmers.co.kr/learn/courses/30/lessons/92335
#k진수에서 소수 개수 구하기
#어려운 것 없음. 제곱근까지 해서 소수 판별하면 빠르다.

def checker(num):
    sqrted = round(num**(1/2))
    for i in range(2, sqrted + 1):
        #print('checking', num, 'with', i)
        if num % i == 0:
            #print('Not Prime on ', i)
            return False
    return True

def solution(n, k):
    answer = 0
    tmp = n
    transferred = ''
    
    while(tmp > k):
        transferred = str(tmp % k) + transferred
        tmp = tmp // k
    transferred = str(tmp) + transferred
    #print(transferred)
    
    numbers = list(map(str, transferred.split('0')))
    
    for num in numbers:
        if num != '1' and num != '':
            if checker(int(num)):
                #print(num)
                answer += 1
    
    return answer