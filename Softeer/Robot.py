import sys

# 그냥 시뮬인듯...?
# 시작점 및 끝점을 찾아보자
h, w = map(int, input().split())
board = [list(input()) for _ in range(h)]
directions = {'>': (0, 1), '<': (0, -1), 'v': (1, 0), '^': (-1, 0)}

start = (-1, -1)
for r in range(h):
    for c in range(w):
        if board[r][c] == '#':
            empty_cnt = 0
            direction = ''
            # 길이 보였다면 4방향 탐색해서 하나만 연결되었는지 확인.
            for dir_exp, dir_go in directions.items():
                dr, dc = dir_go
                nr = dr + r
                nc = dc + c
                # 범위 내인지 확인
                if 0 <= nr < h and 0 <= nc < w:
                    if board[nr][nc] == '.':
                        empty_cnt += 1
                    if board[nr][nc] == '#':
                        direction = dir_exp
                else:
                    empty_cnt += 1
            if empty_cnt == 3:
                start = (r, c, dir_exp)


print(board)
print(start)
"""
# 정해진 시작점에서부터 길을 따라가면 된다.
now_r, now_c = start
while 1:
    # 내가 있는 위치에서 돌면서 방향을 잡는다.


    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        # 두 칸 전진할 수 있을까?
        if 0 <= 2 * dr + now_r < h and 0 <= 2 * dc + now_c < h:
            # 가는 길이 다 #이어야 한다.
            if board[dr + now_r][dc + now_c] == '#' and board[2 * dr + now_r][2 * dc + now_c] == '#':
                # 갈 수 있음 가보자.
                now_r = 2 * dr + now_r
                now_c = 2 * dc + now_c
"""