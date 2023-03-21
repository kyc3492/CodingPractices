#import sys
#sys.setrecursionlimit(10 ** 9)
from copy import deepcopy

# 0. 입력 준비
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

answer = 0

# 90도를 돌려가며 한 방향으로만 움직임을 구현할 것임.
def rotate(board):
    rotated_board = [[0] * n for _ in range(n)]
    for c in range(n):
        for r in range(n):
            rotated_board[c][r] = board[n - r - 1][c]
    return rotated_board


# 움직임을 수행하는 함수
def move(board):
    moved_board = [[0] * n for _ in range(n)] 
    # 좌측으로 밀어오는 함수를 구현할 건데
    # flag는 해당 수를 moved_board에 이미 올려뒀다는 뜻이고
    # idx을 중심으로 하여 target을 움직여가며 더할 수가 있는지 확인
    for r in range(n):
        row = board[r]
        m_row = moved_board[r]
        
        flag = False
        target = -1
        for idx in range(n):
            # 0이라면 다음 idx로 넘어가야한다.
            if row[idx] == 0:
                continue
            # flag가 있는 상황에서 같은 수가 들어왔다면
            if flag == True and row[idx] == m_row[target]:
                # 값을 2배, target 그대로, flag 회수
                m_row[target] *= 2
                flag = False
            # 다른 상황에서는 0이 아닌 다른 값일 때이므로 flag 세우기
            else:
                target += 1
                m_row[target] = row[idx]
                flag = True
                    
    return moved_board
            


# DFS로 다녀왔다 / 롤백했다를 반복
def DFS(board, cnt):
    # 5번의 이동이 모두 수행되었다면
    if cnt == 5:
        global answer
        for i in range(n):
            answer = max(max(board[i]), answer)
        return
    
    # 4군데 각 방향으로 진행
    for _ in range(4):
        # 원래 상황을 얕은 복사 및 돌리기를 수행한다.
        tmp_board = rotate(deepcopy(board))
        # 복사해둔 것으로 이동을 수행한다
        tmp_board = move(tmp_board)
        # 이동이 수행되었다면 다음 이동을 준비한다.
        DFS(tmp_board, cnt + 1)
        # 원상복구한 후 현재 단계에서의 다른 방향으로의 이동을 시도한다.
        # 맨 위에서 얕은 복사를 수행하므로 복구할 필요 없을 듯.
        
DFS(board, 0)
print(answer)