N = int(input())
DP = [0] * (N + 1)
DP[1] = 1
if N > 1:
    DP[2] = 1

for i in range(1, N + 1):
    if i > 2:
        DP[i] += DP[i - 2]
    if i > 1:
        DP[i] += DP[i - 1]

print(DP[N] % 10007)