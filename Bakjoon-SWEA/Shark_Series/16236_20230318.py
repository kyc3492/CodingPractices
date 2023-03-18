# 입력 받기 및 deque 임포트
from collections import deque

n = int(input())
bowl = []
isSharkFound = False
shark_loc = (0, 0)
shark_size = 2
answer = 0
ate = 0
for i in range(n):
    tmp = list(map(int, input().split()))
    if isSharkFound == False:
        for j in range(n):
            if tmp[j] == 9:
                shark_loc = (i, j)
                isSharkFound = True
                break
    bowl.append(tmp)
    
def BFS(shark_loc):
    # 거리를 담을 리스트. 일단 가지 않은 곳은 -1임
    dist_bowl = [[-1] * n for _ in range(n)]
    # 현재 상어 위치를 0으로 초기화
    dist_bowl[shark_loc[0]][shark_loc[1]] = 0
    # 현재 상어의 위치를 큐에 추가
    queue = deque([shark_loc])
    while queue:
        c, r = queue.popleft()
        for dc, dr in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nc = c + dc
            nr = r + dr
            # 다음 위치가 범위 내라면
            if 0 <= nc < n and 0 <= nr < n:
                # 다음 위치가 이동 가능하다면 + 간 적이 없다면
                if bowl[nc][nr] <= shark_size and dist_bowl[nc][nr] == -1:
                    # 직전의 위치에서 1초 더 추가해서 갱신해준다
                    dist_bowl[nc][nr] = dist_bowl[c][r] + 1
                    # 다음 행선지로 추가해준다.
                    queue.append((nc, nr))
    return dist_bowl

# 상어 위치를 받아서 먹이를 찾는 함수
def find_prey(shark_loc):
    # 각 위치까지의 거리를 구해 오면
    dist_bowl = BFS(shark_loc)
    # 현재 최소 거리 먹이를 저장한다.
    dist = n * n
    # 먹이의 유무를 확인한다.
    for i in range(n):
        for j in range(n):
            # 돌면서 먹이와의 거리를 갱신하고 더 적은 거리에 먹이가 있다면 위치와 함께 반환한다.
            # 먹이는 현재 상어보다 작고 거리는 더 적어야 한다. 빈칸이면 안된다.
            if 0 < bowl[i][j] < shark_size and -1 < dist_bowl[i][j] < dist:
                dist = dist_bowl[i][j]
                nc, nr = i, j
    # 거리가 갱신되었다면 반환
    if dist != n * n:
        return dist, nc, nr
    else:
        return 0, 0, 0

# 먹을 수 있는 먹이를 다 먹을 때까지 돈다.
while True:
    dist, nc, nr = find_prey(shark_loc)
    # 거리가 어떻게 반환되었는지 본다.
    if dist != 0:
        # 정답에 추가
        answer += dist
        # 원래 위치는 0
        bowl[shark_loc[0]][shark_loc[1]] = 0
        # 상어 위치 변경
        shark_loc = (nc, nr)
        # 상어가 간 자리도 0
        bowl[nc][nr] = 0
        # 먹은 개수 더해주기
        ate += 1
        # 먹은 개수를 확인하고 size를 키울 수 있는지 확인
        if ate == shark_size:
            ate = 0
            shark_size += 1
    else:
        print(answer)
        break