import sys
from heapq import heappush, heappop
input = sys.stdin.readline

# 명령 수 입력
n = int(input())
heap = []

# 명령 입력
for _ in range(n):
    op = int(input())
    # 출력 명령일 때
    if op == 0:
        if heap == []:
            print(0)
        else:
            print(heappop(heap))
    elif op > 0:
        heappush(heap, op)