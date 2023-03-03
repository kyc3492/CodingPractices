from collections import deque

# 입력을 받고
n = int(input())
bowl = []
shark_loc = []
for i in range(n):
    tmp = list(map(int, input().split()))
    bowl.append(tmp)
    # 입력하는 중에 상어의 존재가 확인된다면
    # 바로 저장
    if 9 in tmp:
        shark_loc = [i, tmp.index(9)]
        bowl[shark_loc[0]][shark_loc[1]] = 0


# 초기 상어 사이즈는 2
shark_size = 2
answer = 0
ate = 0

# 현재 상어 위치에서부터 다른 칸들 까지의 거리를 구해보자.
def cal_dist(shark_loc):
    # 가지 않은 곳은 -1로 해서 초기화
    dist_bowl = [[-1] * n for _ in range(n)]
    dist_bowl[shark_loc[0]][shark_loc[1]] = 0
    # 갈 곳을 지정할 큐를 생성
    queue = deque([(shark_loc[0], shark_loc[1])])
    while queue:
        c, r = queue.popleft()
        for dc, dr in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nc = c + dc
            nr = r + dr
            if 0 <= nc < n and 0 <= nr < n:
                # 가지 않았어야만 + 상어 사이즈 이하여야만 갈 수 있다.
                if dist_bowl[nc][nr] == -1 and bowl[nc][nr] <= shark_size:
                    # 간 적 없으면 직전에서 1번만 더 간 것이므로
                    dist_bowl[nc][nr] = dist_bowl[c][r] + 1
                    queue.append((nc, nr))
    return dist_bowl
                    

# 가장 가까운 먹이까지의 거리를 반환하는 함수
def find(shark_loc):
    # 일단 전체 칸 과의 거리를 구하자.
    dist_bowl = cal_dist(shark_loc)
    # 최소 거리를 위한 최장 거리 지정.
    dist = n * n
    # 전체를 돌면서 먹이를 보자
    # 좌측 + 상단부터 우선순위를 가지는 것이 해결됨.
    for i in range(n):
        for j in range(n):
            # 최소 거리 갱신
            if 0 < bowl[i][j] < shark_size and -1 < dist_bowl[i][j] < dist:
                dist = dist_bowl[i][j]
                nc, nr = i, j
    # 거리 갱신이 안됐다면 0만을 반환
    if dist == n * n:
        return 0, 0, 0
    else:
        bowl[nc][nr] = 0
        return dist, nc, nr
    

# 무한으로 돌리는데
while True:
    # 함수가 가장 가까운 먹이까지의 거리를 반환
    current, nc, nr = find(shark_loc)
    if current != 0:
        shark_loc = [nc, nr]
        answer += current
        ate += 1
        if shark_size == ate:
            shark_size += 1
            ate = 0
    else:
        print(answer)
        break