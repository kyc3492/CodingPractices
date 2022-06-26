from operator import index

n = int(input())
k = int(input())

table = [[0] * (n + 1) for _ in range(n + 1)]
turns = []
index_turns = 0

dx = [0 ,1, 0, -1]
dy = [1, 0, -1, 0]
counter_turns = 0
second_total = 0
body = [[1, 0]]

for _ in range(k):
    x, y = map(int, input().split())
    table[x][y] = 1

table[1][0] = 5
l = int(input())

for _ in range(l):
    x, c = map(str, input().split())
    turns.append([x, c])

def TURNING(second, second_total, turning):
    global counter_turns, index_turns
    #방향전환
    if second == second_total:
        #print("방향 전환")
        index_turns += 1
        if turning == 'D':
            counter_turns += 1
        else:
            counter_turns -= 1

def FORWARD(x, y):
    global second_total, counter_turns, index_turns

    #for l in table:
        #print(l)

    while 1:
        if index_turns < len(turns):
            second = int(turns[index_turns][0])
            turning = turns[index_turns][1]
            #print(second)

        #print("방향전환 안하나")              
        TURNING(second, second_total, turning)
        second_total += 1
        x = x + dx[counter_turns % 4]
        y = y + dy[counter_turns % 4]

        #벽 충돌판정
        if x <= 0 or x > n or y <= 0 or y > n:
            #print("벽 충돌")
            break

        #사과를 먹었다.
        if table[x][y] == 1:
            table[x][y] = 5
            body.append([x, y])
        #몸과 부딪쳤다.
        elif table[x][y] == 5:
            #print("몸 충돌")
            break
        #일반 진행
        else:
            table[x][y] = 5
            body.append([x, y])
            last_x, last_y = body.pop(0)
            table[last_x][last_y] = 0
            #print("정상진행")
            
        #print(second)
        #print(second_total)
        #for l in table:
        #    print(l)

FORWARD(1, 1)
print(second_total)