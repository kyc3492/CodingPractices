# 0. 입력 받기
n = int(input())
total = [card for card in map(int, input().split())]
m = int(input())
sangeun = [card for card in map(int, input().split())]

# 1. 해시 태이블을 만들자. {card: count} -> [핵심]
count = {}
for card in total:
    count[card] = count.setdefault(card, 0) + 1
    """
    위 구문을 풀어쓰면
    
    if card not in count:
        count[card] = 1
    else:
        count[card] += 1
    """

# 2. num 개수를 뽑아보자.
answer = ""
for card in sangeun:
    print(count.setdefault(card, 0), end=" ")
    """
    위 구문을 풀어쓰면
    
    if card not in count:
        answer += str(0) + " "
    else:
        answer += str(count[card]) + " "

이걸 숙지하면 다음처럼 string으로 변환을 굳이 안해도 된다.
print(answer[:-1])
"""