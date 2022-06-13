import math

N = int(input())

GROUND = []
GROUND.append([0] * (N + 4))
GROUND.append([0] * (N + 4))
for i in range(N):
    TMP = []
    TMP.append(0)
    TMP.extend([0])
    TMP.extend(list(map(int, input().split())))
    TMP.extend([0])
    TMP.extend([0])
    GROUND.append(TMP)
GROUND.append([0] * (N + 4))
GROUND.append([0] * (N + 4))

R = int((N + 4)/2)
C = int((N + 4)/2)

DR = [0, 1, 0, -1]
DC = [-1, 0, 1, 0]

#퍼센티지 계산 개노가다...
PERCENTAGE_L = [[0, 0, 0.02, 0, 0],
                [0, 0.1, 0.07, 0.01, 0],
                [0.05, 0, 0, 0, 0],
                [0, 0.1, 0.07, 0.01, 0],
                [0, 0, 0.02, 0, 0]]

PERCENTAGE_R = [[0, 0, 0.02, 0, 0],
                [0, 0.01, 0.07, 0.1, 0],
                [0, 0, 0, 0, 0.05],
                [0, 0.01, 0.07, 0.1, 0],
                [0, 0, 0.02, 0, 0]]

PERCENTAGE_U = [[0, 0, 0.05, 0, 0],
                [0, 0.1, 0, 0.1, 0],
                [0.02, 0.07, 0, 0.07, 0.02],
                [0, 0.01, 0, 0.01, 0],
                [0, 0, 0, 0, 0]]

PERCENTAGE_D = [[0, 0, 0, 0, 0],
                [0, 0.01, 0, 0.01, 0],
                [0.02, 0.07, 0, 0.07, 0.02],
                [0, 0.1, 0, 0.1, 0],
                [0, 0, 0.05, 0, 0],]

#날리기
def TORNADO(R, C, NR, NC, DIRECTION):
    SETTER = []
    #좌하우상으로 방향 전환
    if (DIRECTION % 4) == 0:
        SETTER = list(PERCENTAGE_L)
    elif (DIRECTION % 4) == 1:
        SETTER = list(PERCENTAGE_D)
    elif (DIRECTION % 4) == 2:
        SETTER = list(PERCENTAGE_R)
    elif (DIRECTION % 4) == 3:
        SETTER = list(PERCENTAGE_U)

    ORIGINAL = GROUND[R][C]
    GROUND[R][C] = 0
    SUM_TMP = 0
    for i in range(5):
        for j in range(5):
            if SETTER[i][j] != 0:
                GROUND[R + i - 2][C + j - 2] += math.floor(ORIGINAL * SETTER[i][j])
                SUM_TMP += math.floor(ORIGINAL * SETTER[i][j])
    ORIGINAL -= SUM_TMP
    GROUND[NR][NC] += ORIGINAL


#start에서 일단 이동
MOVEMENT = 1
COUNTER = 0
DIRECTION = 0
FINISHED = False
while 1:
    #2번 움직이면 이동 횟수 1증가 + 방향 바뀜
    if DIRECTION != 0 and DIRECTION % 2 == 0:
        MOVEMENT += 1
    
    for i in range(MOVEMENT):
        #좌하우상으로 방향 전환
        R = R + DR[DIRECTION % 4]
        C = C + DC[DIRECTION % 4]
        #같은 방향으로 한 번 더
        NR = R + DR[DIRECTION % 4]
        NC = C + DC[DIRECTION % 4]
        if GROUND[R][C] != 0:
            TORNADO(R, C, NR, NC, DIRECTION)

        if R < 3 and C < 3:
            FINISHED = True
            break

    DIRECTION += 1
    if FINISHED == True:
        break

ANSWER = 0
for i in range(N + 4):
    for j in range(N + 4):
        if i < 2 or i > (N + 1) or j < 2 or j > (N + 1):
            ANSWER += GROUND[i][j]
print(ANSWER)