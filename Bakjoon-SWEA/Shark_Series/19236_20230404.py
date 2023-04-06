# Python의 DFS는 이제 Stack으로 구현되어야 한다.
# 입력 받기
board = []
# 튜플로 (상어 번호, 방향) 받는다.
for _ in range(4):
    tmp = list(map(int, input().split()))
    shark_idx, shark_dir = 0, 0
    row = []
    for idx in range(8):
        if idx % 2 == 0:
            shark_idx = tmp[idx]
        else:
            shark_dir = tmp[idx] - 1
            row.append((shark_idx, shark_dir))
    board.append(row)

# 최초의 상어 위치는 (0, 0) 이므로
shark_c, shark_r = 0, 0
ate = board[0][0][0]
board[0][0] = (-1, board[0][0][1])
# 현재 상황의 리스트를 스택에 넣어버린다.
stack = [(shark_c, shark_r, board, ate)]
# 방향 idx - 1에 맞도록 방향 리스트 구현
directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]


answer = 0
while stack:
    # 스택 맨 마지막에 있는 상어의 현 위치와 보드의 상황을 불러옴.
    now_c, now_r, ori_board, now_ate = stack.pop()

    # 새 보드를 만든다. 스택에 넣어줄 용도임.
    now_board = [[(0, 0)] * 4 for _ in range(4)]
    for c in range(4):
        for r in range(4):
            now_board[c][r] = ori_board[c][r]

    # 물고기들의 움직임을 구현한다.
    # 작은 물고기부터 이동하면 된다.
    for fish in range(1, 17):
        # 현재 물고기가 이동했던 건가?
        isMoved = False
        for c in range(4):
            if isMoved == True:
                break
            for r in range(4):
                if isMoved == True:
                    break
                # 물고기를 찾았다면
                if now_board[c][r][0] == fish:
                    # 방향을 8번을 돌릴 거임. 45도를 반시계 방향으로 회전할 거임
                    for dir_idx in range(8):
                        now_dir = (now_board[c][r][1] + dir_idx) % 8
                        # 다음 행선지 결정
                        nc = c + directions[now_dir][0]
                        nr = r + directions[now_dir][1]
                        # 범위 내인가?
                        if 0 <= nc < 4 and 0 <= nr < 4:
                            # 빈 칸이 아니고 + 상어가 아니어야 함.
                            if now_board[nc][nr][0] > 0:
                                # 조건 충족한다면 현재 돌려진 방향을 업데이트한 채 해당 행선지의 물고기와 위치 교환
                                # 교환된 위치는 새로운 board로 옮긴다.
                                now_fish = (now_board[c][r][0], now_dir)
                                new_fish = now_board[nc][nr]
                                now_board[nc][nr] = now_fish
                                now_board[c][r] = new_fish
                                # 이동했음을 체크하여 중복 이동을 방지
                                isMoved = True
                        if isMoved == True:
                            break

    # 상어의 움직임을 구현한다.
    # 상어를 움직일 수 있을만큼 (최대 거리 3) 움직인 후 스택에 넣어줌
    now_dir = now_board[now_c][now_r][1]
    # 상어가 움직였는지 채크
    for dist in range(1, 4):
        # 현재에서 배열을 복사
        next_board = [[(0, 0)] * 4 for _ in range(4)]
        for c in range(4):
            for r in range(4):
                next_board[c][r] = now_board[c][r]
        next_c = now_c + (directions[now_dir][0]) * dist
        next_r = now_r + (directions[now_dir][1]) * dist
        # 범위 내인가?
        if 0 <= next_c < 4 and 0 <= next_r < 4:
            # 물고기가 있는가? 빈 칸이면 못 감
            if next_board[next_c][next_r][0] > 0:
                # 먹을 수 있는 물고기가 있다면 상어는 이동한다.
                tmp_ate = next_board[next_c][next_r][0]
                now_ate += tmp_ate
                # 상어 이동
                next_board[next_c][next_r] = (-1, next_board[next_c][next_r][1])
                # 원래 상어 위치는 빈 칸
                next_board[now_c][now_r] = (0, 0)
                # 현 상태를 stack에 추가
                stack.append((next_c, next_r, next_board, now_ate))
                now_ate -= tmp_ate
    # 먹고 현재 먹은 번호 합 갱신
    answer = max(answer, now_ate)
    print(now_ate)

print(answer)