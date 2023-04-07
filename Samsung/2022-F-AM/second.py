from collections import defaultdict

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# [개선할 점] 그룹 id로 이루어진 새로운 리스트를 만들어내면 된다!!
id_board = [[0] * n for _ in range(n)]


def DFS(c, r, gid):
    # 스택 생성
    stack = [(c, r, gid)]
    size = 1
    while stack:
        now_c, now_r, gid = stack.pop()
        # 4방향
        for dc, dr in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_c = now_c + dc
            next_r = now_r + dr
            # 범위 탐색
            if 0 <= next_c < n and 0 <= next_r < n:
                # 이전과 색이 같다면 + 근데 gid 할당이 안되어 있다면
                if board[c][r] == board[next_c][next_r] and id_board[next_c][next_r] == 0:
                    # gid를 할당해주고 스택 업데이트
                    id_board[next_c][next_r] = gid
                    size += 1
                    stack.append((next_c, next_r, gid))
    return size


def make_group():
    # gid: (color, size)
    groups = {}

    gid = 1
    # DFS를 돌 건데 id가 주어지지 않은 곳만 돌 것이다.
    for c in range(n):
        for r in range(n):
            if id_board[c][r] == 0:
                id_board[c][r] = gid
                size = DFS(c, r, gid)
                groups[gid] = (board[c][r], size)
                gid += 1

    print(groups)


rounds = 0
while rounds < 3:

    # 그룹을 만든다.
    make_group()
    
    # 경계를 파악한다.
    # id보드를 돌면서 서로 다르면 +1
    # 단 중복 계산에 유의

    rounds += 1