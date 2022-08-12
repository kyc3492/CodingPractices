import sys
sys.setrecursionlimit(10 ** 9)

N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))
dp = [[-1] * M for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(r, c):
    if r == N - 1 and c == M - 1:
        return 1
    if dp[r][c] != -1:
        return dp[r][c]
    dp[r][c] = 0

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if board[r][c] > board[nr][nc]:
                dp[r][c] += dfs(nr, nc)
    
    '''if r - 1 >= 0:
        if board[r][c] > board[r - 1][c]:
            dp[r][c] += dfs(r - 1, c)
    if r + 1 < N:
        if board[r][c] > board[r + 1][c]:
            dp[r][c] += dfs(r + 1, c)
    if c - 1 >= 0:
        if board[r][c] > board[r][c - 1]:
            dp[r][c] += dfs(r, c - 1)
    if c + 1 < M:
        if board[r][c] > board[r][c + 1]:
            dp[r][c] += dfs(r, c + 1)'''
    return dp[r][c]
    
print(dfs(0, 0))