n, m, k = map(int, input().split())
# 탐색 중에 중복으로 찾아지는 것을 방지하기 위해 팀 머리 dict를 생성
teams = {}
board = []
team_idx = 1
for c in range(n):
    tmp = list(map(int, input().split()))
    for r in range(n):
        if tmp[r] == 1:
            teams[team_idx] = (c, r)
            team_idx += 1
    board.append(tmp)

directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def move_team(c, r):
    # c, r은 머리의 위치를 찾았으니
    # 주변을 돌면서 비어있는 길을 찾는다.
    # 스택을 구성해서 좌표를 하나씩 넣어주면 될 듯?
    stack = [(c, r, c, r)]
    while stack:
        # 스택에서 가장 마지막 것을 가져온다.
        now_c, now_r, next_c, next_r = stack.pop()
        # 머리십니까?
        if now_c == next_c and now_r == next_r:
            # 4방향 탐색
            for dc, dr in directions:
                nc = now_c + dc
                nr = now_r + dr
                # 범위 내인가
                if 0 <= nc < n and 0 <= nr < n:
                    # 길인가?
                    if board[nc][nr] == 4:
                        # 나아가자
                        board[nc][nr] = board[now_c][now_r]
                        # 현 위치에서는 길을 터준다
                        board[now_c][now_r] = 4
                        # 머리 위치 갱신
                        teams[team_idx] = (nc, nr)
                    # 몸통 혹은 꼬리였다면
                    elif 1 < board[nc][nr] < 4:
                        # 특수한 상황에 대비. 꼬리와 맞다아 있을 수 있음.
                        if board[nc][nr] == 3:
                            # 이 경우엔 꼬리로 1을 옮기고 3을 나아가게 해야함.
                            head = (now_c, now_r)
                            tail = (nc, nr)
                            for ndc, ndr in directions:
                                nnc = nc + ndc
                                nnr = nr + ndr
                                if 0 <= nnc < n and 0 <= nnr < n:
                                    # 3은 다음 2로 나아가게 한다
                                    if board[nnc][nnr] == 2:
                                        board[nnc][nnr] = 3
                                        board[nc][nr] = 1
                                        # 머리 위치 갱신
                                        board[now_c][now_r] = 2
                                        teams[team_idx] = (nc, nr)
                                        # 특수한 상황으로 끝내버림
                                        return
                        # 스택에 추가해서 또 찾을 수 있도록 해준다.
                        # 현재의 위치를 추가하면서 쉽게 길을 찾도록 해주자.
                        stack.append((nc, nr, now_c, now_r))
        # 몸통이나 꼬리인가?
        else:
            # 그리고 본인이 몸통인가?
            if board[now_c][now_r] == 2:
                # 4방향 탐색해서 다음 사람 위치 탐색
                for dc, dr in directions:
                    nc = now_c + dc
                    nr = now_r + dr
                    # 범위 내인가
                    if 0 <= nc < n and 0 <= nr < n:
                        if 1 < board[nc][nr] < 4:
                            # 스택에 추가해서 또 찾을 수 있도록 해준다.
                            # 현재의 위치를 추가하면서 쉽게 길을 찾도록 해주자.
                            stack.append((nc, nr, now_c, now_r))
                            break
            # 몸통, 꼬리 공통
            # next_c, next_r로 위치를 바꿔주고 길을 터줌
            board[next_c][next_r] = board[now_c][now_r]
            board[now_c][now_r] = 4


def hit_team(c, r):
    # 순서를 반환하고. 머리와 꼬리를 바꾸는 함수
    order = -1
    head = (0, 0)
    tail = (0, 0)
    if board[c][r] == 1:
        head = (c, r)
    elif board[c][r] == 3:
        tail = (c, r)
    # 머리인가? 머리라면 1을 반환
    if board[c][r] == 1:
        order = 1
    # 아니라면 stack을 활용해서 몇 번째인지 확인하러 간다.
    stack = [(c, r, 1)]
    history = []
    while stack:
        now_c, now_r, now_order = stack.pop()
        # 왔다감.
        history.append((now_c, now_r))
        # 4방향 탐색
        for dc, dr in directions:
            next_c = now_c + dc
            next_r = now_r + dr
            if 0 <= next_c < n and 0 <= next_r < n:
                # 처음 가보는 데인가?
                if (next_c, next_r) not in history:
                    # 몸통의 연속인가?
                    if board[next_c][next_r] == 2:
                        # 스택에 추가. 번째 수 포함해서
                        stack.append((next_c, next_r, now_order + 1))
                    # 머리가 나왔나?
                    if board[next_c][next_r] == 1:
                        # 현재 순번과 맞은 팀을 반환
                        order = now_order + 1
                        head = (next_c, next_r)
                    if board[next_c][next_r] == 3:
                    # 꼬리가 나왔나?
                        tail = (next_c, next_r)
    # 보드에 머리, 꼬리 교체 반영
    board[head[0]][head[1]] = 3
    board[tail[0]][tail[1]] = 1
    # 어떤 팀이 맞았는지 볼까?
    for team_idx in range(1, m + 1):
        if teams[team_idx] == head:
            # 해당 팀의 머리 변경
            teams[team_idx] = tail

    return order


answer = 0
rounds = 0
while rounds < k:
    # 1칸 이동을 구현한다.
    team_idx = 1
    while team_idx < m + 1:
        # 각 팀의 머리를 찾는다.
        c, r = teams[team_idx]
        # 이동을 구현하는 함수
        move_team(c, r)
        team_idx += 1

    # 라운드 별 공 던지기를 구현한다.
    # 라운드가 n을 넘어가는 기점에 따라 directions가 달라진다.
    # directions는 0~3 idx를 가진다.
    # [c][r] -> c가 증가해서 n에 도달하면[0] / r도 증가해서 n에 도달하면[1] / c를 감소해서 0에 도달하면[2] / r도 감소해서 0에 도달하면[3]
    if (rounds // n) % 4 == 0:
        ball_c = rounds % (n * 4)
        ball_r = 0
        ball_dir = directions[(rounds // n) % 4]
    elif (rounds // n) % 4 == 1:
        ball_c = n - 1
        ball_r = (rounds % (n * 4)) - n
        ball_dir = directions[(rounds // n) % 4]
    elif (rounds // n) % 4 == 2:
        ball_c = (n - 1) - ((rounds % (n * 4)) - 2 * n)
        ball_r = n - 1
        ball_dir = directions[(rounds // n) % 4]
    elif (rounds // n) % 4 == 3:
        ball_c = 0
        ball_r = (n - 1) - ((rounds % (n * 4)) - 3 * n)
        ball_dir = directions[(rounds // n) % 4]

    # 일단 발사
    dist = 1
    while 1:
        # 거리가 넘어가면 끝냄
        if dist > n + 1:
            break
        # 유효한가
        if 0 <= ball_c < n and 0 <= ball_r < n:
            # 누군가 맞았다면, 몇 번째인지 체크해야되네
            if 0 < board[ball_c][ball_r] < 4:
                order = hit_team(ball_c, ball_r)
                answer += (order * order)
                break
        dist += 1
        ball_c += ball_dir[0]
        ball_r += ball_dir[1]
    rounds += 1

print(answer)