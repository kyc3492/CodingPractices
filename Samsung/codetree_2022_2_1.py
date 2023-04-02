# 입력 받기
# 1 -> 베이스캠프, 2 -> 편의점 위치
n, m = map(int, input().split())
board = []
# 베이스캠프 위치를 받아둠.
basecamp = []
for c in range(n):
    tmp = list(map(int, input().split()))
    board.append(tmp)
    for r in range(n):
        if tmp[r] == 1:
            basecamp.append((c, r))

# 편의점 위치도 받아둠.
convi = []
for i in range(m):
    c, r = map(int, input())
    convi.append((c, r))
    board[c][r] = 2

# 정해진 편의점 위치를 저장해둘 거임.
#     
dest = []
# 무한으로 돌아보자.
answer = 0
while 1:
    # bfs로 가장 가까운 편의점의 거리가 나올 거임.
    # 그걸 기반으로 처음 m분 동안은 각자의 목적지를 정한다.
    if answer < m:
        find_near()