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
            shark_dir = tmp[idx]
            row.append((shark_idx, shark_dir))
    board.append(row)

# 최초의 상어 위치는 (0, 0) 이므로
shark_c, shark_r = 0, 0
answer = board[0][0][0]
board[0][0] = (-1, board[0][0][1])
# 현재 상황의 리스트를 스택에 넣어버린다.
copied_board = [[(0, 0)] * 4 for _ in range(4)]
for c in range(4):
    for r in range(4):
        copied_board[c][r] = board[c][r]
stack = [(shark_c, shark_r, copied_board)]
# 방향 idx - 1에 맞도록 방향 리스트 구현
directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

while stack:
    # 스택 맨 마지막에 있는 상어의 현 위치와 보드의 상황을 불러옴.
    now_c, now_r, now_board = stack.pop()
    
    # 물고기들의 움직임을 구현한다.
    # 작은 물고기부터 이동하면 된다.
    for c in range(4):
        for r in range(4):
            # 방향을 8번을 돌릴 거임. 45도를 반시계 방향으로