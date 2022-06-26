N = int(input())
Board = [[0] * N for _ in range(N)]

def Attack_Range(r, c):
    global Board
    for i in range(N):
        Board[i][c] = 1
        Board[r][i] = 1
    tmp_r = r
    tmp_c = c
    while 1:
        tmp_r += 1
        tmp_c += 1
        if tmp_r >= 0 and tmp_r < N and tmp_c >= 0 and tmp_c < N:
            Board[tmp_r][tmp_c] = 1
        else:
            break
    tmp_r = r
    tmp_c = c
    while 1:
        tmp_r -= 1
        tmp_c -= 1
        if tmp_r >= 0 and tmp_r < N and tmp_c >= 0 and tmp_c < N:
            Board[tmp_r][tmp_c] = 1
        else:
            break
    tmp_r = r
    tmp_c = c
    while 1:
        tmp_r += 1
        tmp_c -= 1
        if tmp_r >= 0 and tmp_r < N and tmp_c >= 0 and tmp_c < N:
            Board[tmp_r][tmp_c] = 1
        else:
            break
    tmp_r = r
    tmp_c = c
    while 1:
        tmp_r -= 1
        tmp_c += 1
        if tmp_r >= 0 and tmp_r < N and tmp_c >= 0 and tmp_c < N:
            Board[tmp_r][tmp_c] = 1
        else:
            break
    

Answer = 0
start_r = 0
start_c = 0
while 1:
    print("Starting...", start_r, start_c)
    Board = [[0] * N for _ in range(N)]
    Counter = 0
    index_r = start_r
    index_c = start_c
    while Counter < N:
        if Board[index_r][index_c] == 0:
            Counter += 1
            if Counter == N - 1:
                Answer += 1
                break
            print("Checking...", index_r, index_c)
            Attack_Range(index_r, index_c)
            print("Counter...", Counter)
            index_r += 1
            if index_r == N:
                index_c += 1
                index_r = 0
            if index_c == N:
                break
        else:
            index_r += 1
            if index_r == N:
                index_c += 1
                index_r = 0
            if index_c == N:
                break
    start_r += 1
    if start_r == N:
        start_c += 1
        start_r = 0
    if start_c == N:
        break

print(Answer)