from itertools import combinations
# 0. 입력받기. 조합을 이용.

n, m = map(int, input().split())
cards = list(map(int, input().split()))

# 1. 3개씩 조합을 뽑아 더하면서 크기 체크
answer = 0
for selected in combinations(cards, 3):
    if sum(selected) <= m:
        answer = max(sum(selected), answer)
        
print(answer)