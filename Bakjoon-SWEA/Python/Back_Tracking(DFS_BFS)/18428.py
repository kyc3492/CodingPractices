import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())

table = []
data_T = []
data_S = []
data_X = []
result_WATCH = []
result = False

for i in range(n):
    table.append(list(map(str, input().split())))
    for j in range(n):
        if table[i][j] == 'T':
            data_T.append((i, j))
        elif table[i][j] == 'S':
            data_S.append((i, j))
        else:
            data_X.append((i, j))
            
#감시되나 안되나 다 보는 함수. 발각되면 TRUE, 못보면 FALSE
#좌, 상, 우, 하 순임.
def WATCH(x, y, direction):
    if direction == 0:
        while y >= 0:
            if table[x][y] == 'S':
                return True
            if table[x][y] == 'O':
                return False
            y -= 1
    
    if direction == 1:
        while x >= 0:
            if table[x][y] == 'S':
                return True
            if table[x][y] == 'O':
                return False
            x -= 1

    if direction == 2:
        while y < n:
            if table[x][y] == 'S':
                return True
            if table[x][y] == 'O':
                return False
            y += 1

    if direction == 3:
        while x < n:
            if table[x][y] == 'S':
                return True
            if table[x][y] == 'O':
                return False
            x += 1

#찾는 함수
def WATCH_PROCESS():
    for x_T, y_T in data_T:
        for i in range(4):
            if WATCH(x_T, y_T, i):
                return True
    return False

#장애물 설치하기
#빈 공간에서 임의 3개 장소 뽑기 + 감시 되나 안되나 확인
for free_space in combinations(data_X, 3):
    for x_X, y_X in free_space:
        table[x_X][y_X] = 'O'
        #print(data_O)
        
    #감시되는지 확인하는 절차b 
    if WATCH_PROCESS() == False:
        result = True
        break

    #감시가 되었으면 다시, 안되었으면 답변 출력
    for x_X, y_X in data_X:
        result_WATCH = False
        table[x_X][y_X] = 'X'
        
    #print(table)

if result == True:
    print('YES')
else:
    print('NO')