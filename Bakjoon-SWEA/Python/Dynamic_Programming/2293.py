N, K = map(int, input().split())
Coin = []
for i in range(N):
    Coin.append(int(input()))

Memo = [0] * (K + 1)
Memo[0] = 1

for i in range(N):
    for j in range(Coin[i], K + 1):
        Memo[j] += Memo[j - Coin[i]]

print(Memo[K])