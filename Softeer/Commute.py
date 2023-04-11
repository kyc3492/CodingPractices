import sys

# n은 노드, m은 간선의 개수
n, m = map(int, input().split())
roads = [[] for _ in range(n + 1)]
roadsR = [[] for _ in range(n + 1)]

# 간선 입력. idx번에서 갈 수 있는 길이 있음을 표기함.
for _ in range(m):
    s, d = map(int, input().split())
    roads[s].append(d)
    roadsR[d].append(s)

# 집과 회사 위치에 해당하는 정점 번호 확인
home, work = map(int, input().split())

# DFS를 활용한 문제. 스택을 활용해볼 수 있겠다.
# 최초에는 집 위치를 넣고 돌면서 -> 목적지를 지나지 않고 갈 수 있는 곳을 모두 체크
def path_finder(start, roads, route):
    stack = [start]
    while stack:
        now_loc = stack.pop()
        if route[now_loc]:
            continue
        route[now_loc] = 1
        for next_loc in roads[now_loc]:
            stack.append(next_loc)        
    return

print(roads)
print(roadsR)

route_to_work = [0 for _ in range(n + 1)]
route_to_work[work] = 1
path_finder(home, roads, route_to_work)
print(route_to_work)

route_to_home = [0 for _ in range(n + 1)]
route_to_home[home] = 1
path_finder(work, roads, route_to_home)
print(route_to_home)

route_from_work = [0 for _ in range(n + 1)]
path_finder(work, roadsR, route_from_work)
print(route_from_work)

route_from_home = [0 for _ in range(n + 1)]
path_finder(home, roadsR, route_from_home)
print(route_from_home)

# 두 리스트에서 겹치는 부분의 합을 구한다.
answer = 0
for idx in range(1, n + 1):
    if route_to_work[idx] and route_to_home[idx] and route_from_work[idx] and route_from_home[idx]:
        answer += 1
print(answer - 2)