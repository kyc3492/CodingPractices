import sys
sys.setrecursionlimit(100000)

n = int(input())
minimum = 100
maximum = 0
city = [list(map(int, input().split())) for _ in range(n)]

for r in city:
    minimum = min(min(r), minimum)
    maximum = max(max(r), maximum)
    
dc = [-1, 1, 0, 0]
dr = [0, 0, -1, 1]
def DFS(c, r, rain):
    visited[c][r] = True
    for d in range(4):
        nc = c + dc[d]
        nr = r + dr[d]
        if range_checker(nc, nr) and city[nc][nr] > rain and visited[nc][nr] == False:
            DFS(nc, nr, rain)

def range_checker(c, r):
    if 0 <= c < n and 0 <= r < n:
        return True
    else:
        return False
    
safe_zone = -1
for rain in range(minimum, maximum + 1):
    current = 0
    visited = [[False] * n for _ in range(n)]
    for c in range(n):
        for r in range(n):
            if visited[c][r] == False and city[c][r] > rain:
                DFS(c, r, rain)
                current += 1
    safe_zone = max(safe_zone, current)

if safe_zone == 0:
    print(1)
else:
    print(safe_zone)