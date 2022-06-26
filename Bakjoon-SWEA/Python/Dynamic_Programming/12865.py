N, K = map(int, input().split())

Things = []
for i in range(N):
    Things.append(list(map(int, input().split())))

Memo = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j - Things[i - 1][0] >= 0:
            Memo[i][j] = max(Memo[i - 1][j], Memo[i - 1][j - Things[i - 1][0]] + Things[i - 1][1])
        else:
            Memo[i][j] = Memo[i - 1][j]
    
print(Memo[N][K])