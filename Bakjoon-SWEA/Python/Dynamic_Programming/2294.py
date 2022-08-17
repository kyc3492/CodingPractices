n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
coins = sorted(coins, reverse=True)
cnt = -1

#테이블 만들어 돌리기
dp = [10001] * (k + 1)
dp[0] = 0
for i in range(n):
    for j in range(coins[i], (k + 1)):
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])

#dfs -> 시간 초과
'''def dfs():
    global n, k, coins, cnt, Min
    i = 0

    if k == 0:
        #print(cnt + 1)
        if Min == -1:
            Min = cnt + 1
        else:
            Min = min(cnt + 1, Min)
        return Min
    elif k < 0:
        return -1
    else:
        if cnt + 2 < Min or Min == -1:
            while i < n:
                if k % coins[i] == 0:
                    dp[i] = k // coins[i]
                    cnt = dp[i]
                else:
                #print("Using Coin", coins[i], k)
                    k -= coins[i]
                    cnt += 1
                    dfs()
                    cnt -= 1
                    k += coins[i]
                    #print("Unusing Coin", coins[i], k)
                    i += 1
    return Min

print(dfs())'''
#print(cnt)