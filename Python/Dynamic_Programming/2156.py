N = int(input())
Wine = []
for _ in range(N):
    Wine.append(int(input()))
DP = [0] * N
DP[0] = Wine[0]

for i in range(1, N):
    if i - 3 >= 0:
        DP[i] = max(Wine[i] + Wine[i - 1] + DP[i - 3], Wine[i] + DP[i - 2], DP[i - 1])
    if i == 2:
        DP[i] = max(Wine[i] + Wine[i - 1], Wine[i] + DP[i - 2], DP[i - 1])
    if i == 1:
        DP[i] = Wine[i] + Wine[i - 1]

print(max(DP))