N = int(input())
T = []
P = []

for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
T.append(0)
P.append(0)
#print(T)
#print(P)

DP = [0] * (N + 1)
for i in range(N + 1):
    print("Looking day", i)
    for j in range(i - 1, -1, -1):
        print(DP)
        if j + T[j] <= i:
            print("Finished Time of", j)
            DP[i] = max(DP[i], DP[j] + P[j])

print(DP[-1])