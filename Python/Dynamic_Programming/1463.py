X = int(input())
DP = [0] * 10000001
DP[1] = 0
DP[2] = 1
DP[3] = 1

if X > 3:
    for i in range(4, X + 1):
        DP[i] = DP[i - 1] + 1
        if i % 2 == 0:
            DP[i] = min(DP[int(i / 2)] + 1, DP[i])
        if i % 3 == 0:
            DP[i] = min(DP[int(i / 3)] + 1, DP[i])

print(DP[X])