# 0. 입력을 받고
n = int(input())
bowl = []
shark_size = 2
cnt = 0
shark_loc = []

for i in range(n):
    tmp = list(map(int, input().split()))
    if 9 in tmp:
        # 상어 위치를 파악.
        shark_loc = (i, tmp.index(9))
    bowl.append(tmp)

answer = 0
dc = [-1, 1, 0, 0]
dr = [0, 0, -1, 1]
# 1. 현재 상어의 크기를 고려하여 먹을 수 있는 먹이들 중에서
# 2. BFS로 거리를 구해 최소한으로 갈 수 있는지를 파악.

def find_topleft(queue, n):
    tmp = []
    for c, r in queue:
        tmp.append(c * n + r)
    tmp.sort()
    tl_c = tmp[0] // n
    tl_r = tmp[0] % n
    return tl_c, tl_r

def checker(c, r, bowl, shark_size, n, history):
    if 0 <= c < n and 0 <= r < n:
        if history[c][r] != 1:
            if bowl[c][r] <= shark_size:
                return True
    return False

# 찾는 함수
def find_next(n, shark_loc, bowl, shark_size):
    queue = [shark_loc]
    history = [[0] * n for _ in range(n)]
    history[shark_loc[0]][shark_loc[1]] = 1
    for dist in range(1, n * n):
        nextQueue = []
        edibleQueue = []
        for c, r in queue:
            for d in range(4):
                nc = c + dc[d]
                nr = r + dr[d]
                if checker(nc, nr, bowl, shark_size, n, history):
                    nextQueue.append((nc, nr))
                    history[nc][nr] = 1
                    if 0 < bowl[nc][nr] < shark_size:
                        edibleQueue.append((nc, nr))
        # 먹을 수 있는 게 있다면
        # 상어 위치를 이동하고 지금 위치를 반환
        if len(edibleQueue) != 0:
            c, r = find_topleft(edibleQueue, n)
            bowl[shark_loc[0]][shark_loc[1]] = 0
            bowl[c][r] = 9
            return dist, (c, r)
        if len(nextQueue) == 0:
            return 0, (0, 0)
        queue = nextQueue
    
# 거리가 0으로 나오는 경우 -> 갈 곳이 없을 경우까지 계속 돌린다.
while True:
    current, shark_loc = find_next(n, shark_loc, bowl, shark_size)
    if current == 0:
        print(answer)
        break
    # 먹은 먹이 개수에 따른 상어 사이즈 반영
    cnt += 1
    if cnt == shark_size:
        shark_size += 1
        cnt = 0
    answer += current