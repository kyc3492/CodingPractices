import sys
sys.setrecursionlimit(1000000)

N = int(input())
Board = []
Board_RG = []

for _ in range(N):
    Board.append(input())

for i in range(N):
    tmp = ''
    for j in range(N):
        if Board[i][j] == "R" or Board[i][j] == "G":
            tmp += "R"
        else:
            tmp += Board[i][j]
    Board_RG.append(tmp)

Zone = [[-1] * N for _ in range(N)]
Zone_RG = [[-1] * N for _ in range(N)]

dc = [-1, 0, 1, 0]
dr = [0, 1, 0, -1]
#start = Board[0][0]

def dfs(c, r, Board, Zone):
    Zone[c][r] = 1
    current = Board[c][r]
    for i in range(4):
        nc = c + dc[i]
        nr = r + dr[i]

        if 0 <= nc < N and 0 <= nr < N:
            if Zone[nc][nr] == -1:
                if Board[nc][nr] == current:
                    dfs(nc, nr, Board, Zone)
                #else:
                    #print("Different!", nc, nr)
                    #print(Zone)
                    #return

cnt = 0
for i in range(N):
    for j in range(N):
        if Zone[i][j] == -1:
            dfs(i, j, Board, Zone)
            cnt += 1

#print("Normal")
print(cnt)

cnt_RG = 0
for i in range(N):
    for j in range(N):
        if Zone_RG[i][j] == -1:
            dfs(i, j, Board_RG, Zone_RG)
            cnt_RG += 1
#print("RG")
print(cnt_RG)