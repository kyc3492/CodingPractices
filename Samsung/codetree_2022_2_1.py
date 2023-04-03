from collections import deque

# 입력 받기
n, m = map(int, input().split())
# 지도 정보를 받을 건데
# 베이스캠프 -> 1
board = []
# 베이스캠프도 큐로 받아둘 거임. 최상단+좌측부터.
# 그러다 할당되면 지울라고
basecamps = deque([])
for c in range(n):
    tmp = list(map(int, input().split()))
    board.append(tmp)
    for r in range(n):
        if tmp[r] == 1:
            basecamps.append((c, r))
            
# 편의점 위치 정보를 받을 건데
# 모양은 idx: c, r
convis = {}
for i in range(m):
    c, r = map(int, input().split())
    convis[i] = (c - 1, r - 1)

# 고객 정보를 저장할 거임.
# idx: c, r, 도착 여부
customers = {}
directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def find_near():
    # 현재 찾을 편의점 idx를 받는다. 결국 answer임
    convi_c, convi_r = convis[answer]
    # 후보군 리스트 (거리, 베이스c, 베이스r)
    candi = []
    # 큐 생성. 최초는 각 베이스캠프에서의 위치
    for base_c, base_r in basecamps:
        # 베이스캠프는 할당되어있지 않아야 함.
        if board[base_c][base_r] != -1:
            queue = deque([(base_c, base_r)])
            # 거리 리스트. 초기값 -1
            dist = [[-1] * n for _ in range(n)]
            dist[base_c][base_r] = 0
            while queue:
                c, r = queue.popleft()
                # 4방향 탐색
                for d in range(4):
                    nc = c + directions[d][0]
                    nr = r + directions[d][1]
                    # 범위 내인지 확인
                    if 0 <= nc < n and 0 <= nr < n:
                        # 갈 수 있는 곳인지 + 처음 가는 곳인지
                        if dist[nc][nr] == -1 and board[nc][nr] != -1:
                            # 거리 구하고 큐에 추가
                            dist[nc][nr] = dist[c][r] + 1
                            queue.append((nc, nr))
                            # 우선순위대로 가다가 편의점이 발견되면
                            if nc == convi_c and nr == convi_r:
                                # 일단 후보군으로 넣는다.
                                candi.append((dist[nc][nr], base_c, base_r))
    # 단거리순으로 일단 정렬
    sorted_candi = sorted(candi)
    return (sorted_candi[0][1], sorted_candi[0][2])
    """
    minimum_dist = sorted_candi[0][0]
    mini_candi = []
    # 단거리가 여러 개인지 확인
    for candi_idx in range(len(sorted_candi)):
        if sorted_candi[candi_idx] == minimum_dist:
            mini_candi.append(sorted_candi[candi_idx])
    # 한 개라면 그거 반환하면 되고
    if len(mini_candi) == 1:
        return (mini_candi[1], mini_candi[2])
    # 아니라면 상, 좌, 우, 하 반영
    else:
    """    
                

def move_step(idx, cust_c, cust_r):
    # 현재 받아온 손님의 위치에서 4방향을 구해놓자
    candis = []
    result = (0, 0, n ** n)
    
    for d in range(4):
        nc = cust_c + directions[d][0]
        nr = cust_r + directions[d][1]
        # 범위 내라면 후보군에 일단 추가
        if 0 <= nc < n and 0 <= nr < n:
            # 갈 수 있는 곳인지까지 확인하고
            if board[nc][nr] != -1:
                if nc == convis[idx][0] and nr == convis[idx][1]:
                    # 한 발짝 움직였는데 바로 그 곳에 편의점이 있을 수 있음
                    result = (nc, nr, 1)
                # 아쉽게 아니라면 후보군 등록
                else:
                    candis.append((nc, nr))
                    
    # 결과가 갱신됐다는 뜻은 이미 답을 찾았다는 것
    if result == (0, 0, n ** n):    
        for now_c, now_r in candis:
            # 큐 생성. 최초는 현재 후보군의 위치
            queue = deque([(now_c, now_r)])
            # 거리 리스트. 초기값 -1
            dist = [[-1] * n for _ in range(n)]
            dist[now_c][now_r] = 0
            while queue:
                c, r = queue.popleft()
                # 4방향 탐색
                for d in range(4):
                    nc = c + directions[d][0]
                    nr = r + directions[d][1]
                    # 범위 내인지 확인
                    if 0 <= nc < n and 0 <= nr < n:
                        # 갈 수 있는 곳인지 + 처음 가는 곳인지
                        if dist[nc][nr] == -1 and board[nc][nr] != -1:
                            # 거리 구하고 큐에 추가
                            dist[nc][nr] = dist[c][r] + 1
                            queue.append((nc, nr))
                            # 우선순위대로 가다가 맞는 편의점이 나오면
                            if nc == convis[idx][0] and nr == convis[idx][1]:
                                # 그 편의점으로 가는 최적의 경로인지 판단하고
                                if result[2] > dist[nc][nr]:
                                    result = (now_c, now_r, dist[nc][nr])
    
    # 다 돌고나면 최적의 방향을 반환
    return result


# 모든 손님이 편의점에 도착할 때까지 돌 거임.
arrived = 0
answer = 0
while arrived < m:
    bumper = 0
    # 경과한 분(answer)이 손님 수(m)보다 작다면 베이스캠프 할당이 우선임.
    if answer < m:
        # customer dict에 최초 위치(베이스캠프)를 지정해 줄 함수
        new_c, new_r = find_near()
        # 할당 되면 -1 처리로 못 지나가게도 해야됨.
        board[new_c][new_r] = -1
        # 고객 정보를 저장한다.
        customers[answer] = (new_c, new_r, False)
        bumper = 1
    # 이제 각 고객을 돌면서 위치를 갱신해주어야 함.
    # 단 같은 시간에 추가된 고객은 제외해야하므로
    for cust_idx in range(len(customers) - bumper):
        # 4방향으로 한 칸씩 움직인 후 어느 쪽으로 가야 제일 빠를지 판단하는 함수
        # 하나 할 때마다 board에 편의점 도착 여부를 파악하고 반영해야 함.
        if customers[cust_idx][2] == False:
            next_c, next_r, _ = move_step(cust_idx, customers[cust_idx][0], customers[cust_idx][1])
            # 고객 위치 갱신
            customers[cust_idx] = (next_c, next_r, False)
            # 다음 위치가 편의점 위치와 같다면?
            if next_c == convis[cust_idx][0] and next_r == convis[cust_idx][1]:
                # 도착 여부 갱신하고 못가게 막기
                customers[cust_idx] = (next_c, next_r, True)
                board[convis[cust_idx][0]][convis[cust_idx][1]] = -1
                arrived += 1
        
    answer += 1

print(answer)