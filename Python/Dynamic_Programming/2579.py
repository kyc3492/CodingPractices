N = int(input())
Stairs = []
for i in range(N):
    Stairs.append(int(input()))

DP = [[0] * 2 for i in range(N)]
DP[0][0] = Stairs[0]

for i in range(1, N):
    if i - 1 > 0:
        DP[i][0] = max(DP[i - 2][1] + Stairs[i], DP[i - 2][0] + Stairs[i])
    else:
        DP[i][0] = 0 + Stairs[i]
    DP[i][1] = DP[i - 1][0] + Stairs[i]

print(max(DP[N - 1]))