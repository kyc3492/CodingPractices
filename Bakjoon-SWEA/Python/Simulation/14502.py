from itertools import combinations
import copy

n, m = map(int, input().split())
lab = []
space = []
virus = []
for i in range(n):
    lab.append(list(map(int, input().split())))
    for j in range(m):
        if lab[i][j] == 0:
            space.append([i, j])
        if lab[i][j] == 2:
            virus.append([i, j])
            
lab_simulated = copy.deepcopy(lab)
#print(id(lab_simulated))
#print(id(lab))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
best_case = -1
this_case = 0

#바이러스 감염
def SPREAD(x, y):
    for j in range(4):
        #print(lab_simulated)
        nx = x + dx[j]
        ny = y + dy[j]
        #print(nx, ny)
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if lab_simulated[nx][ny] == 0:
                lab_simulated[nx][ny] = 2
                #print(lab_simulated)
                SPREAD(nx, ny)

#안전구역 체크
def SAFETY_CHECK():
    global this_case
    virus_simulated = copy.deepcopy(virus)
    for i in virus_simulated:
        x, y = i
        #print(x, y)
        SPREAD(x, y)
    #print(lab_simulated)
    for i in range(n):
        for j in range(m):
            if lab_simulated[i][j] == 0:
                this_case += 1

#print(lab)
#벽 세우기
for added_wall in combinations(space, 3):
    for i in range(3):
        x_aw, y_aw = added_wall[i]
        lab_simulated[x_aw][y_aw] = 1
    SAFETY_CHECK()
    if this_case > best_case:
        best_case = this_case
    this_case = 0
    lab_simulated = copy.deepcopy(lab)

print(best_case)
#print(lab)
