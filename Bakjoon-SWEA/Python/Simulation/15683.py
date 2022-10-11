def DFS(CCTV, Office):
    global Zeros

    tmp_Office = [0] * N
    if CCTV == len(Cameras):
        tmp_cnt = 0
        for i in range(N):
            tmp_cnt += Office[i].count(0)

        #print(tmp_cnt)
        Zeros = min(tmp_cnt, Zeros)

        return

    for i in range(N):
        tmp_Office[i] = Office[i][:]
    
    c, r, each_mode = Cameras[CCTV]
    for D in Mode[each_mode]:
        Searching(tmp_Office, c, r, D)
        DFS(CCTV + 1, tmp_Office)
        for i in range(N):
            tmp_Office[i] = Office[i][:]

def Searching(tmp_Office , c, r, D):
    for d in D:
        if d == 0:
            for mc in range(c, -1, -1):
                #print("Filling", mc, r, d)
                if tmp_Office[mc][r] == 6:
                    #print("Met Wall")
                    break
                if tmp_Office[mc][r] == 0:
                    tmp_Office[mc][r] = 9
        elif d == 1:
            for mc in range(c, N):
                #print("Filling", mc, r, d)
                if tmp_Office[mc][r] == 6:
                    #print("Met Wall")
                    break
                if tmp_Office[mc][r] == 0:
                    tmp_Office[mc][r] = 9
        elif d == 2:
            for mr in range(r, -1, -1):
                #print("Filling", c, mr, d)
                if tmp_Office[c][mr] == 6:
                    #print("Met Wall")
                    break
                if tmp_Office[c][mr] == 0:
                    tmp_Office[c][mr] = 9
        elif d == 3:
            for mr in range(r, M):
                #print("Filling", c, mr, d)
                if tmp_Office[c][mr] == 6:
                    #print("Met Wall")
                    break
                if tmp_Office[c][mr] == 0:
                    tmp_Office[c][mr] = 9    


N, M = map(int, input().split())
mod_Office = [0] * N
Office = []
Cameras = []
Zeros = 0
for i in range(N):
    Office.append(list(map(int, input().split())))
    for j in range(M):
        if Office[i][j] != 0 and Office[i][j] != 6:
            Cameras.append([i, j, Office[i][j]])
        elif Office[i][j] == 0:
            Zeros += 1

Cameras = sorted(Cameras, key = lambda x : x[2], reverse = True)

Mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]], 
    [[0, 2], [0, 3], [1, 2], [1, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]

DFS(0, Office)

print(Zeros)