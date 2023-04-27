import sys
from heapq import heappush, heappop
input = sys.stdin.readline

# 카드 묶음 수
n = int(input())
heap = []

# 각 카드 묶음 입력
for _ in range(n):
    heappush(heap, int(input()))

# 최종 비교 수
result = 0

# 카드 뭉치가 최종 하나만 나올 때까지
while len(heap) > 1:
    # A + B를 구현함.
    # 맨 앞 카드 뭉치 두 개를 가져와 합친다.
    A = heappop(heap)
    B = heappop(heap)
    
    # 최종 결과에 추가한다.
    result += A + B
    # 현재 만들어진 카드 뭉치를 heap큐에 추가한다.
    # 원래 그냥 계속 더하는 것으로 해결보려 했는데 틀려서 이를 해결함.
    # 다음과 같은 예외 상황을 해결할 수 있음.
    # 2, 2, 3, 3 -> 4, 3, 3 (4) -> 7, 3 (11) -> 10 (21) X
    # 가장 적은 수의 카드 뭉치가 합쳐지는 게 아니기 때문에 오답.
    # 2, 2, 3, 3 -> 3, 3, 4 (4) -> 4, 6 (10) -> 10 (20) O
    heappush(heap, A + B)
    
print(result)