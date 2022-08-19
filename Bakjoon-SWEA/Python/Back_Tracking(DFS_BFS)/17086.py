from collections import deque

ans = 0
N, M = map(int, input().split())
Board = []
for _ in range(N):
    Board.append(list(map(int, input().split())))

dc = [-1, 1, 0, 0, 1, 1, -1, -1]
dr = [0, 0, -1, 1, 1, -1, 1, -1]

Shark = deque()
for i in range(N):
    for j in range(M):
        if Board[i][j] == 1:
            Shark.append([i, j])

def bfs():
    while Shark:
        c, r = Shark.popleft()
        for i in range(8):
            nc = c + dc[i]
            nr = r + dr[i]
            if 0 <= nc < N and 0 <= nr < M:
                if Board[nc][nr] == 0:
                    Shark.append([nc, nr])
                    Board[nc][nr] = Board[c][r] + 1
    return

bfs()
for i in range(N):
    for j in range(M):
        ans = max(ans, Board[i][j])

'''for i in range(N):
    for j in range(M):
        print(Board[i][j], end=" ")
    print()
'''
print(ans - 1)