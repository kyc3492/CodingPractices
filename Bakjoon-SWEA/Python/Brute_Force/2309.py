# 0. 조합을 이용. 입력 준비
from itertools import combinations

dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))

# 1. 조합을 돌려보며 답 찾기
answer = 0
for real in combinations(dwarfs, 7):
    if sum(real) == 100:
        answer = real
        break

# 2. 오름차순으로 세로로 출력
for i in sorted(answer):
    print(i)