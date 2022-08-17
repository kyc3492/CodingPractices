import sys
input = sys.stdin.readline

T = int(input())
Final = -1

def dfs(Board, W, N, D, DP):
    global Final
    hasNextNode = False

    for i in range(N):
        #print(DP)
        if Board[i][W - 1] == 1:
            hasNextNode = True
            if D[i] + DP[W - 1] > DP[i]:
                DP[i] = DP[W - 1] + D[i]
                #print("Contructing...", W, "To", i + 1, "(", D[W - 1], D[i],")")
                dfs(Board, i + 1, N, D, DP)
    
    if hasNextNode == False:
        #print("Final Contructing...", W)
        #DP[W - 1] += D[W - 1]
        Final = W - 1

    return

for test_case in range(T):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    DP = [-1] * N
    
    Board = [[0] * N for _ in range(N)]
    for i in range(K):
        s, d = map(int, input().split())
        Board[s-1][d-1] = 1

    W = int(input())
    DP[W - 1] = D[W - 1]

    dfs(Board, W, N, D, DP)
    #print(test_case ,"TEST CASE ANSWER", DP[Final])
    print(DP[Final])
    
    #print(Board)