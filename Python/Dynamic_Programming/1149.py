N = int(input())
DP = [[0] * 3 for _ in range(N)]
for i in range(N):
    DP[i] = list(map(int, input().split()))

for i in range(1, N):
    DP[i][0] += min(DP[i - 1][1], DP[i - 1][2])
    DP[i][1] += min(DP[i - 1][0], DP[i - 1][2])
    DP[i][2] += min(DP[i - 1][0], DP[i - 1][1])

print(sorted(DP[N - 1])[0])