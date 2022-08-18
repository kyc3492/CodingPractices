from collections import deque

M, N, H = map(int, input().split())
Space = []
for _ in range(H):
    tmp = []
    for _ in range(N):
        tmp.append(list(map(int, input().split())))
    Space.append(tmp)

Riped = deque()
for h in range(H):
    for i in range(N):
        for j in range(M):
            if Space[h][i][j] == 1:
                Riped.append([h, i, j])

dh = [0, 0, 0, 0, -1, 1]
dc = [-1, 0, 1, 0, 0, 0]
dr = [0, 1, 0, -1, 0, 0]

while Riped:
    h = Riped[0][0]
    c = Riped[0][1]
    r = Riped[0][2]

    for i in range(6):
        nh = h + dh[i]
        nc = c + dc[i]
        nr = r + dr[i]
        
        if 0 <= nc < N and 0 <= nr < M and 0 <= nh < H:
            if Space[nh][nc][nr] == 0:
                Riped.append([nh, nc, nr])
                Space[nh][nc][nr] = Space[h][c][r] + 1
    Riped.popleft()

    #print(Space)
    #print(Riped)

ans = -1
isZero = False
for h in range(H):
    if isZero == True:
        break
    else:
        for i in range(N):
            if isZero == True:
                break
            else:
                for j in range(M):
                    if Space[h][i][j] == 0:
                        isZero = True
                        ans = -1
                        break
                    else:
                        ans = max(ans, Space[h][i][j] - 1)

print(ans)