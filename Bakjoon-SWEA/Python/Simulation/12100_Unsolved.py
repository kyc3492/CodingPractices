def Range_Checker(c, r):
    if 0 <= c < N and 0 <= r < N:
        return True
    else:
        return False

def Game_Over(Board):
    Max_Block = 0
    for c in range(N):
        for r in range(N):
            if Board[c][r] > 0:
                Max_Block = max(Board[c][r], Max_Block)
    return Max_Block

def Game_Start(Board, Round):
    if Round == 2:
        return Game_Over(Board)

    # 4가지 방향인데 각 방향 때마다 배열 새로해야됨.
    for d in range(4):
        tmp_Board = [0] * N
        for i in range(N):
            tmp_Board[i] = Board[i][:]
        for k in range(N):
                print(tmp_Board[k])
        print("Now Round", Round, "Direction", d)
        # 각 방향에 따라 모든 블럭들을 움직어야함.
        for c in range(N):
            for r in range(N):
                # 빈 칸은 넘기고
                if tmp_Board[c][r] != 0:
                    nc = c + dc[d]
                    nr = r + dr[d]
                    # 범위 체크
                    if Range_Checker(nc, nr):
                        print("Checking", c, r)
                        # 다음거랑 같은 숫자면 해당 칸은 0, 다음 칸은 두 배
                        if tmp_Board[c][r] == tmp_Board[nc][nr]:
                            print("Same With", nc, nr)
                            tmp_Board[c][r] = 0
                            tmp_Board[nc][nr] *= 2
                        # 빈칸이면 그 방향 끝으로 가야됨.
                        elif tmp_Board[nc][nr] == 0:
                            nnc = nc
                            nnr = nr
                            while tmp_Board[nnc][nnr] == 0 and Range_Checker(nnc, nnr) == True:
                                nnc += dc[d]
                                nnr += dr[d]
                            print("Filling", nnc, nnr)
                            tmp_Board[c][r] = 0
                            tmp_Board[nnc - dc[d]][nnr - dr[d]] = tmp_Board[c][r]

        Max_Block = Game_Start(tmp_Board, Round + 1)
    
    return Max_Block


N = int(input())
Board = []
for i in range(N):
    Board.append(list(map(int, input().split())))

dc = [-1, 0, 1, 0]
dr = [0, 1, 0, -1]

print(Game_Start(Board, 0))