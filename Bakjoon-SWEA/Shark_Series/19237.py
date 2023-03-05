# 입력 받기
n, m, k = map(int, input().split())
# 격자의 모양 입력 받기
board = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    # 상어인 경우에는 냄새를 반영해주어야 함.
    new_tmp = []
    for t in tmp:
        if t > 0:
            new_tmp.append((t, k))
        else:
            new_tmp.append((0, 0))
    board.append(new_tmp)
# 바라보는 방향을 상, 하, 좌, 우의 순서로 적어두는데, 0부터 시작할거임.
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 상어의 번호대로 현재 바라보는 방향을 입력 받기
looking = list(map(int, input().split()))
# 각 상어의 방향 순서를 기록한다. 기록표에서도 역시 0부터 시작할거임.
# 즉, 1번 상어의 우선순위는 0번이 되는 것임.
sharks_priority = [list(list(map(int, input().split())) for _ in range(4)) for _ in range(m)]

answer = 0
remained = m
# 전체가 1000초가 넘으면 -1을 출력하는 조건에 따라.
while answer < 1001:
    # 변화를 주기 전 직전 상태를 저장함.
    prev_board = [[(0, 0)] * n for _ in range(n)]
    for c in range(n):
        for r in range(n):
            prev_board[c][r] = board[c][r]    
    # 상어의 이동은 작은 숫자와 큰 숫자가 만나면 큰 숫자가 사라지는 방식이므로
    # 큰 숫자부터 진행 -> 작은 숫자가 온다면 덮어쓰기 방식으로 1까지 돌리면 된다.
    for shark in range(m, 0, -1):
        isMoved = False
        # 공간에서 상어 찾기. n은 최대가 20이므로 따로 좌표를 저장하지 않았고
        # 처음부터 찾는 걸 반복하려고 한다.
        for c in range(n):
            for r in range(n):
                # 상어 본체가 있다는 것은 냄새도 k 그대로 있음을 명심.
                if board[c][r] == (shark, k):
                    # 찾았으니 이동해야지. 현재 바라보고 있는 방향에 따른 이동 방향을 찾아주고.
                    # -1 하는 것을 계속 생각해야함. 괴랄함...
                    # 우선순위 리스트를 가져오면 0번째부터 차례로 확인한다.
                    # 일단 빈 칸으로 갈 수 있는지를 확인한다.
                    for d in sharks_priority[shark - 1][looking[shark - 1] - 1]:
                        dc, dr = directions[d - 1]
                        nc = c + dc
                        nr = r + dr
                        # 공간을 벗어나지 않는다면
                        if 0 <= nc < n and 0 <= nr < n:
                            # 다음 공간이 빈 칸이라면
                            if board[nc][nr] == (0, 0):
                                # 상어를 이동합시다.
                                board[nc][nr] = (board[c][r][0], k + 1)
                                # 상어의 바라보는 방향도 갱신
                                looking[shark - 1] = d
                                isMoved = True
                                break
                            # 아니면 현재보다 큰 번호의 상어가 존재한다면 쫒아내고 가도 됨.
                            # 단, 이 경우엔 직전에 빈 칸이었어야 함.
                            # 동시에 다같이 움직이고 함께 한 공간에 있는 경우에 쫒아낼 수 있는데,
                            # 이를 확인하지 않는다면, 다른 상어의 냄새가 이미 있었음에도 쫒아내러 가는 경우가 발생. -> 반례임.
                            if board[nc][nr][0] > board[c][r][0] and board[nc][nr][1] == k + 1 and prev_board[nc][nr] == (0, 0):
                                # 상어를 이동합시다.
                                board[nc][nr] = (board[c][r][0], k + 1)
                                # 상어의 바라보는 방향도 갱신
                                looking[shark - 1] = d
                                # 이렇게 사라진 상어가 몇 마리인지 확인
                                remained -= 1
                                isMoved = True
                                break
                    
                    # 전체 방향을 다 돌았는데도 불구하고 이동이 없었다면 -> 본인 냄새가 있던 곳으로 가자
                    if isMoved == False:
                        for d in sharks_priority[shark - 1][looking[shark - 1] - 1]:
                            dc, dr = directions[d - 1]
                            nc = c + dc
                            nr = r + dr
                            # 공간을 벗어나지 않는다면
                            if 0 <= nc < n and 0 <= nr < n:
                                # 다음 공간이 내 냄새가 있는 칸이라면
                                if board[nc][nr][0] == shark:
                                    # 상어를 이동합시다.
                                    board[nc][nr] = (board[c][r][0], k + 1)
                                    # 상어의 바라보는 방향도 갱신
                                    looking[shark - 1] = d
                                    break
                                    
    # 다 돌고 냄새 정리
    for c in range(n):
        for r in range(n):
            if board[c][r] != (0, 0):
                if board[c][r][1] > 1:
                    board[c][r] = (board[c][r][0], board[c][r][1] - 1)
                else:
                    board[c][r] = (0, 0)
    
    answer += 1
    if remained == 1:
        break

if answer == 1001:
    print(-1)
else:
    print(answer)