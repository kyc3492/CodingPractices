DP = [0] * (11)
DP[1] = 1
DP[2] = 1
DP[3] = 1

for i in range(1, 11):
    if i > 3:
        DP[i] += DP[i - 3]
    if i > 2:
        DP[i] += DP[i - 2]
    if i > 1:
        DP[i] += DP[i - 1]

T = int(input())
for _ in range(T):
    N = int(input())
    print(DP[N])
