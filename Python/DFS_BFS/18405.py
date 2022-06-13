import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

table = []
data = []

for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    table.append(list(map(int, input().split())))
    for j in range(n):
        if table[i][j] != 0:
            data.append((table[i][j], 0, i, j))

target_time, target_x, target_y = map(int, input().split())

data.sort()
q = deque(data)

while q:
    virus, time, x, y = q.popleft()
    
    if time == target_time:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if table[nx][ny] == 0:
                table[nx][ny] = virus
                print(table)
                q.append([virus, time + 1, nx, ny])

print(table[target_x - 1][target_y - 1])