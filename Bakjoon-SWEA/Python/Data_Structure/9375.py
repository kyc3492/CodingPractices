# 0. 입력 준비
# defaultdict로 dict 자료형을 좀 더 편하게 사용할 수 있다.
from collections import defaultdict
import math
import sys
input = sys.stdin.readline

# 테스트케이스 분기
T = int(input())
for testcase in range(T):
    # 1. 옷 카테고리별 몇 벌인지 기록한다. 어떤 옷인지는 무관하므로 개수만 기록한다.
    n = int(input())
    closet = defaultdict(int)
    # defaultdict는 0일 때를 감안하지 않아도 된다. 기존에 closet = {} 로 선언했다면,
    # 초기값은 1, 다음에 입력 받을 때는 += 1로 분기를 나누어야 했다.
    # defaultdict는 해당 키가 값을 가지지 않는다면 자동으로 0을 반환하므로,
    for _ in range(n):
        _, category = map(str, input().split())
        # 다음과 같이 += 1로 퉁칠 수 있다.
        closet[category] += 1
        
    # 2. 아주 약간의 수학이 들어간다.
    # 각각의 카테고리의 의상을 모두 고를 수 있지만 안 고르는 경우도 고려하여 각 의상 개수 + 1
    # 단, 최소 한 가지 카테고리는 입어야하므로 전체 개수에서 -1
    answer = math.prod(value + 1 for _, value in closet.items()) - 1
        
    print(answer)