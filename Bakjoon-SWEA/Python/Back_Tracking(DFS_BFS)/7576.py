from collections import deque

M, N = map(int, input().split())
Space = []
for _ in range(N):
    Space.append(list(map(int, input().split())))

Riped = deque()
for i in range(N):
    for j in range(M):
        if Space[i][j] == 1:
            Riped.append([i, j])

dc = [-1, 0, 1, 0]
dr = [0, 1, 0, -1]

while Riped:
    c = Riped[0][0]
    r = Riped[0][1]

    for i in range(4):
        nc = c + dc[i]
        nr = r + dr[i]
        
        if 0 <= nc < N and 0 <= nr < M:
            if Space[nc][nr] == 0:
                Riped.append([nc, nr])
                Space[nc][nr] = Space[c][r] + 1
    Riped.popleft()

    #print(Space)
    #print(Riped)

ans = -1
isZero = False
for i in range(N):
    if isZero == True:
        break
    else:
        for j in range(M):
            if Space[i][j] == 0:
                isZero = True
                ans = -1
                break
            else:
                ans = max(ans, Space[i][j] - 1)

print(ans)
'''def dfs(c, r, day):
    for i in range(4):
        nc = c + dc[i]
        nr = r + dr[i]
        
        if 0 <= nc < N and 0 <= nr < M:
            if Space[nc][nr] == 0:
                Space[nc][nr] = Space[c][r] + 1
                print(Space, day)
                day = dfs(nc, nr, day)
        day += 1
    return day
    
for c, r in Riped:
    print(dfs(c, r, 0))'''