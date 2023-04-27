from heapq import heappop, heappush
import sys
input = sys.stdin.readline

# 입력 개수 받기
n = int(input())

# 힙을 두 개를 쓸 것이다.
# 작은 절반들의 최대 힙.
maximum_of_smallers = []
# 큰 절반들의 최소 힙
minimum_of_largers = []

# 하나씩 수를 받는다.
for _ in range(n):
    now = int(input())
    # 수를 받고 나면 일단 두 힙 중에 고른다.
    # 작은 쪽이라면 + 총 길이가 짝수인 경우 두 수 중 작은 수라는 조건에 의해
    if not maximum_of_smallers:
        heappush(maximum_of_smallers, now * -1)
    else:
        if now * -1 >= maximum_of_smallers[0]:
            heappush(maximum_of_smallers, now * -1)
        # 큰 쪽이라면
        else:
            heappush(minimum_of_largers, now)
        
    # 양 쪽의 크기를 맞춰준다. 둘이 같거나 작은 쪽이 하나 더 많아야 됨.
    if len(maximum_of_smallers) < len(minimum_of_largers):
        move_to_small = heappop(minimum_of_largers) * -1
        heappush(maximum_of_smallers, move_to_small)
    elif len(maximum_of_smallers) > len(minimum_of_largers) + 1:
        move_to_large = heappop(maximum_of_smallers) * -1
        heappush(minimum_of_largers, move_to_large)
    
    print(maximum_of_smallers[0] * -1)