N, M, K = map(int, input().split())
FIREBALLS = []
for i in range(M):
    FIREBALLS.append(list(map(int, input().split())))

FIELD = [[0] * N for i in range(N)]

DR = [-1, -1, 0, 1, 1, 1, 0, -1]
DC = [0, 1, 1, 1, 0, -1, -1, -1]

while 1:
    #파이어볼 위치에 저장
    FIELD = [[0] * N for i in range(N)]
    for i in range(M):
        R = (FIREBALLS[i][0] - 1) % 4
        C = (FIREBALLS[i][1] - 1) % 4
        FIELD[R][C] = FIREBALLS[i][2]
    
    #이동 및 결합까지만
    SUM_D = 0
    SUM_COUNTER = 0
    SUM_S = 0
    D_SPREAD = []
    FIREBALLS_SPREAD = []
    for i in range(len(FIREBALLS)):
        S = FIREBALLS[i][3]
        D = FIREBALLS[i][3]
        NR = (R + (DR[D] * S)) % 4
        NC = (C + (DC[D] * S)) % 4
        
        #없으면 입력
        if FIELD[NR][NC] == 0:
            FIELD[NR][NC] = FIREBALLS[i][2]
            SUM_D = FIREBALLS[i][4]
            SUM_COUNTER += 1

        #있으면 더하기
        else:
            FIELD[NR][NC] += FIREBALLS[i][2]
            DIVIDED = FIELD[NR][NC] / 5
            SUM_COUNTER += 1
            SUM_D += FIREBALLS[i][4]
            if SUM_D % 2 == 0:
                D_SPREAD = [0, 2, 4, 6]
            else:
                D_SPREAD = [1, 3, 5, 7]
            
    
    for j in range(4):
        SR = (NR + (D_SPREAD[i] * S)) % 4
        SC = (NC + (D_SPREAD[i] * S)) % 4
        FIELD[SR][SC] = SUM_D / SUM_COUNTER

    break

print(FIELD)