N = int(input())

if N > 1:
    DP = [0] * (N + 1)
    DP[0] = 0
    DP[1] = 1
    DP[2] = 1
    # DP[3] -> DP[2] + DP[1] = 2
    # 100, 101
    # DP[4] -> DP[3] + DP[2] = 3
    # 1000, 1001, 1010
    # DP[5] -> DP[4] + DP[3] = 5
    # 10000, 10001, 10010, 10100, 10101

    for i in range(2, N + 1):
        DP[i] = DP[i - 1] + DP[i - 2]

    print(DP[N])
else:
    print(1)