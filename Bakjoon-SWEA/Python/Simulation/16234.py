import math

n, l, r = map(int, input().split())
alliance = []
isThereMovement = True
day = 0

world = []
for _ in range(n):
    world.append(list(map(int, input().split())))

#오른쪽이랑 아래만 보면 됨
dx = [1, 0]
dy = [0, 1]

#n씩 돌면서 각 칸 간 차이 파악 -> 너비탐색
def CREATE_ALLIANCE(x, y):
    print("CREATE_ALLIANCE")
    global n, alliance, isThereMovement, day
    alliance_tmp = []

    for i in range(2):
        x_tmp = x + dx[i]
        y_tmp = y + dy[i]
        #l, r 사이인지 파악
        if x_tmp >= 0 and x_tmp < n and y_tmp >= 0 and y_tmp < n:
            if abs(world[x_tmp][y_tmp] - world[x][y]) >= l and abs(world[x_tmp][y_tmp] - world[x][y]) <= r:
                #처음에 만족하면 [0, 0]도 연합 포함.
                print(x, y)
                if x == 0 and y == 0:
                    alliance_tmp.append([x, y])
                if [x_tmp, y_tmp] not in alliance:
                    alliance_tmp.append([x_tmp, y_tmp])
                    alliance += alliance_tmp
                    day += 1
    
    #추가 연합 맺기가 없으면 루프 종료
    if len(alliance_tmp) == 0 and x == (n - 1) and y == (n - 1):
        return False

                

#연합끼리 평균 구해서 보드에 적용
def MOVE():
    print("MOVE")
    global alliance, world
    sum = 0 
    average = 0
    for x, y in alliance:
        sum += world[x][y]
        average = sum / len(alliance)
    for x, y in alliance:
        world[x][y] = math.floor(average)

while 1:
    for i in range(n):
        for j in range(n):
            CREATE_ALLIANCE(i, j)
            #if CREATE_ALLIANCE(i, j) == False:
            #    isThereMovement = False
    MOVE()
    print(alliance)
    print(world)
    print(isThereMovement)
    if isThereMovement == False:
        break
    #다음날 루프 시작

print(day)
