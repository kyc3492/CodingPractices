# 단순 깡구현. 조건대로 구현하는 내구력을 길러보자

# 0. 입력 준비
n, m, c, r, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ops = list(map(int, input().split()))

# 1. 주사위를 준비한다.
# 바닥은 (1, 1)을 고정토록 한다
dice = [[0] * 3 for _ in range(4)]
dice_loc = (c, r)

for op in ops:
    # 동쪽으로 이동한다면
    if op == 1:
        # 다음 전개도를 생성해두고
        next_dice = [[0] * 3 for _ in range(4)]
        # 주사위 위치는 동쪽으로 한 칸
        c, r = dice_loc
        nc = c
        nr = r + 1
        # 이 위치가 가능한 위치인지 확인
        if 0 <= nc < n and 0 <= nr < m:
            # 주사위 위치 갱신
            dice_loc = (nc, nr)
            # 다음 전개도를 그려준다.
            # 바닥은 (1, 1) -> (1, 0)으로 이동한다.
            next_dice[0][1] = dice[0][1]
            next_dice[1][0] = dice[1][1]
            next_dice[1][1] = dice[1][2]
            next_dice[1][2] = dice[3][1]
            next_dice[2][1] = dice[2][1]
            next_dice[3][1] = dice[1][0]
            # 현재 바닥이 0이라면
            if board[nc][nr] == 0:
                # 바닥면의 수를 복사한다.
                board[nc][nr] = next_dice[1][1]
            # 0이 아니라면
            else:
                # 칸의 수를 가져간다.
                next_dice[1][1] = board[nc][nr]
                board[nc][nr] = 0
            # 상단의 값을 출력한다.
            print(next_dice[3][1])
            # 전개도를 갱신한다.
            dice = next_dice
        else:
            continue
    
    # 서쪽으로 이동한다면
    elif op == 2:
        # 다음 전개도를 생성해두고
        next_dice = [[0] * 3 for _ in range(4)]
        # 주사위 위치는 서쪽으로 한 칸
        c, r = dice_loc
        nc = c
        nr = r - 1
        # 이 위치가 가능한 위치인지 확인
        if 0 <= nc < n and 0 <= nr < m:
            # 주사위 위치 갱신
            dice_loc = (nc, nr)
            # 다음 전개도를 그려준다.
            # 바닥은 (1, 1) -> (1, 2)으로 이동한다.
            next_dice[0][1] = dice[0][1]
            next_dice[1][0] = dice[3][1]
            next_dice[1][1] = dice[1][0]
            next_dice[1][2] = dice[1][1]
            next_dice[2][1] = dice[2][1]
            next_dice[3][1] = dice[1][2]
            # 현재 바닥이 0이라면
            if board[nc][nr] == 0:
                # 바닥면의 수를 복사한다.
                board[nc][nr] = next_dice[1][1]
            # 0이 아니라면
            else:
                # 칸의 수를 가져간다.
                next_dice[1][1] = board[nc][nr]
                board[nc][nr] = 0
            # 상단의 값을 출력한다.
            print(next_dice[3][1])
            # 전개도를 갱신한다.
            dice = next_dice
        else:
            continue
        
    # 북쪽으로 이동한다면
    elif op == 3:
        # 다음 전개도를 생성해두고
        next_dice = [[0] * 3 for _ in range(4)]
        # 주사위 위치는 북쪽으로 한 칸
        c, r = dice_loc
        nc = c - 1
        nr = r
        # 이 위치가 가능한 위치인지 확인
        if 0 <= nc < n and 0 <= nr < m:
            # 주사위 위치 갱신
            dice_loc = (nc, nr)
            # 다음 전개도를 그려준다.
            # 바닥은 (1, 1) -> (2, 1)으로 이동한다.
            next_dice[0][1] = dice[3][1]
            next_dice[1][0] = dice[1][0]
            next_dice[1][1] = dice[0][1]
            next_dice[1][2] = dice[1][2]
            next_dice[2][1] = dice[1][1]
            next_dice[3][1] = dice[2][1]
            # 현재 바닥이 0이라면
            if board[nc][nr] == 0:
                # 바닥면의 수를 복사한다.
                board[nc][nr] = next_dice[1][1]
            # 0이 아니라면
            else:
                # 칸의 수를 가져간다.
                next_dice[1][1] = board[nc][nr]
                board[nc][nr] = 0
            # 상단의 값을 출력한다.
            print(next_dice[3][1])
            # 전개도를 갱신한다.
            dice = next_dice
        else:
            continue
        
    # 남쪽으로 이동한다면
    elif op == 4:
        # 다음 전개도를 생성해두고
        next_dice = [[0] * 3 for _ in range(4)]
        # 주사위 위치는 남쪽으로 한 칸
        c, r = dice_loc
        nc = c + 1
        nr = r
        # 이 위치가 가능한 위치인지 확인
        if 0 <= nc < n and 0 <= nr < m:
            # 주사위 위치 갱신
            dice_loc = (nc, nr)
            # 다음 전개도를 그려준다.
            # 바닥은 (1, 1) -> (0, 1)으로 이동한다.
            next_dice[0][1] = dice[1][1]
            next_dice[1][0] = dice[1][0]
            next_dice[1][1] = dice[2][1]
            next_dice[1][2] = dice[1][2]
            next_dice[2][1] = dice[3][1]
            next_dice[3][1] = dice[0][1]
            # 현재 바닥이 0이라면
            if board[nc][nr] == 0:
                # 바닥면의 수를 복사한다.
                board[nc][nr] = next_dice[1][1]
            # 0이 아니라면
            else:
                # 칸의 수를 가져간다.
                next_dice[1][1] = board[nc][nr]
                board[nc][nr] = 0
            # 상단의 값을 출력한다.
            print(next_dice[3][1])
            # 전개도를 갱신한다.
            dice = next_dice
        else:
            continue