N, M = map(int, input().split())
board = []
answer = 0

def checker(n, m):
    global answer

    #(4 x 1)
    if n + 3 < N:
        answer = max(board[n][m] + board[n + 1][m] + board[n + 2][m] + board[n + 3][m], answer)
    #(3 x 2)
    if n + 2 < N and m + 1 < M:
        answer = max(board[n][m] + board[n + 1][m] + board[n + 2][m] + board[n + 2][m + 1], answer) #ㄱ자
        answer = max(board[n][m] + board[n + 1][m] + board[n + 2][m] + board[n + 1][m + 1], answer) #T자 모양
        answer = max(board[n][m] + board[n + 1][m] + board[n + 1][m + 1] + board[n + 2][m + 1], answer) #ㄹ자 모양
        answer = max(board[n][m] + board[n][m + 1] + board[n + 1][m + 1] + board[n + 2][m + 1], answer) #ㄴ자
    #(2 x 3)
    if n + 1 < N and m + 2 < M:
        answer = max(board[n][m] + board[n + 1][m] + board[n + 1][m + 1] + board[n + 1][m + 2], answer) #ㄱ자
        answer = max(board[n][m] + board[n][m + 1] + board[n][m + 2] + board[n + 1][m + 1], answer) #T수직
        answer = max(board[n][m] + board[n][m + 1] + board[n + 1][m + 1] + board[n + 1][m + 2], answer) #ㄹ수직
        answer = max(board[n][m] + board[n][m + 1] + board[n][m + 2] + board[n + 1][m + 2], answer) #ㄴ자
    #(2 x 2)
    if n + 1 < N and m + 1 < M:
        answer = max(board[n][m] + board[n + 1][m] + board[n][m + 1] + board[n + 1][m + 1], answer)

    #반대로. 순서동일
    if n - 3 >= 0:
        answer = max(board[n][m] + board[n - 1][m] + board[n - 2][m] + board[n - 3][m], answer)
    if n - 2 >= 0 and m + 1 < M:
        answer = max(board[n][m] + board[n - 1][m] + board[n - 2][m] + board[n - 2][m + 1], answer) #ㄱ자
        answer = max(board[n][m] + board[n - 1][m] + board[n - 2][m] + board[n - 1][m + 1], answer) #T자 모양
        answer = max(board[n][m] + board[n - 1][m] + board[n - 1][m + 1] + board[n - 2][m + 1], answer) #ㄹ자 모양
        answer = max(board[n][m] + board[n][m + 1] + board[n - 1][m + 1] + board[n - 2][m + 1], answer) #ㄴ자
    if n - 1 >= 0 and m + 2 < M:
        answer = max(board[n][m] + board[n - 1][m] + board[n - 1][m + 1] + board[n - 1][m + 2], answer) #ㄱ자
        answer = max(board[n][m] + board[n][m + 1] + board[n][m + 2] + board[n - 1][m + 1], answer) #T자
        answer = max(board[n][m] + board[n][m + 1] + board[n - 1][m + 1] + board[n - 1][m + 2], answer) #ㄹ수직
        answer = max(board[n][m] + board[n][m + 1] + board[n][m + 2] + board[n - 1][m + 2], answer) #ㄴ자
    if n - 1 < N and m + 1 < M:
        answer = max(board[n][m] + board[n - 1][m] + board[n][m + 1] + board[n - 1][m + 1], answer)

    #(1 x 4)
    if m + 3 < M:
        answer = max(board[n][m] + board[n][m + 1] + board[n][m + 2] + board[n][m + 3], answer)
    #T자 거꾸로
    if m + 1 < M and n - 1 >= 0 and n + 1 < N:
        answer = max(board[n][m] + board[n - 1][m + 1] + board[n][m + 1] + board[n + 1][m + 1], answer)


for n in range(N):
    board.append(list(map(int, input().split())))

for n in range(N):
    for m in range(M):
        checker(n, m)

#print(N, M)
#print(board)
print(answer)