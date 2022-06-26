T = int(input())
for _ in range(T):
    N = int(input())
    
    Coin = list(map(int, input().split()))

    M = int(input())

    Memo = [0] * (M + 1)
    Memo[0] = 1

    for i in range(N):
        for j in range(Coin[i], M + 1):
            Memo[j] += Memo[j - Coin[i]]
    
    print(Memo[M])