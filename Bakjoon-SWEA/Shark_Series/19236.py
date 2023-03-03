# 일단 순서에 맞게 방향 배열을 만들자
directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

# 물고기 공간 받기
original_bowl = []
for _ in range(4):
    row = []
    tmp = list(map(int, input().split()))
    for idx in range(8):
        if idx % 2 == 1:
            # (물고기 번호, 방향 - 1) 모양으로 받아준다. 방향 리스트 인덱스와 맞추기 위해.
            row.append((tmp[idx - 1], tmp[idx] - 1))
    original_bowl.append(row)

# (0, 0) 부터 먹고 들어가기 때문에
answer = original_bowl[0][0][0]
original_bowl[0][0] = (-1, original_bowl[0][0][1])

# 물고기가 이동하는 함수
def move_fish(bowl):
    # 물고기는 다행히도 1 ~ 16까지임. 작은 물고기부터 이동
    for f in range(1, 17):
        # 물고기가 찾아졌다면 다음으로 넘어가야지
        finish_move = False
        for c in range(4):
            for r in range(4):
                # 물고기를 찾으면
                if bowl[c][r][0] == f:
                    # 방향 체크하고 이동 가능한지 확인
                    d = bowl[c][r][1]
                    while True:
                        # 현재 방향에서 진행했을 때 범위 밖으로 나가지 않는다면 + 상어가 아니라면
                        if 0 <= c + directions[d][0] < 4 and 0 <= r + directions[d][1] < 4 and bowl[c + directions[d][0]][r + directions[d][1]][0] > -1:
                            fish_next_c = c + directions[d][0]
                            fish_next_r = r + directions[d][1]
                            break
                        # 나간다면
                        else:
                            d = (d + 1) % 8
                    # 이동 가능해지면, 그 위치에 있는 것과 바꿔야지
                    fish_tmp = bowl[fish_next_c][fish_next_r]
                    # 단 방향이 바뀌어 있을 수 있다는 것에 유의
                    bowl[fish_next_c][fish_next_r] = (bowl[c][r][0], d)
                    bowl[c][r] = fish_tmp
                    finish_move = True
                if finish_move:
                    break
            if finish_move:
                break
    return bowl
                        

# 상어가 이동하는 함수. 갈 수 있는 방법이 많을 것이므로 DFS로 구현
def move_shark(prev_bowl, current, ate):
    global answer
    # 현재 배열을 "진정한" 얕은 복사 해야함.
    bowl = [[(0, 0)] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            bowl[i][j] = prev_bowl[i][j]
    # 물고기를 이동시키고
    bowl = move_fish(bowl)
    shark_now_c, shark_now_r = 0, 0
    find_shark = False
    for i in range(4):
        for j in range(4):
            # 상어를 찾자.
            if bowl[i][j][0] == -1:
                shark_now_c = i
                shark_now_r = j
                find_shark = True
            if find_shark:
                break
        if find_shark:
            break
    # 상어의 방향도 가지고 오자
    shark_direction = directions[bowl[shark_now_c][shark_now_r][1]]
    # 상어가 움직일 수 없는 경우는 막다른 길이거나 + 방향에 물고기가 없거나
    for len in range(1, 4):
        shark_next_c = shark_now_c + (shark_direction[0] * len)
        shark_next_r = shark_now_r + (shark_direction[1] * len)
        # 범위 내라면
        if 0 <= shark_next_c < 4 and 0 <= shark_next_r < 4:
            # 그리고 물고기가 있다면
            if bowl[shark_next_c][shark_next_r][0] > 0:
                # 그 물고기를 먹고
                current += bowl[shark_next_c][shark_next_r][0]
                # 이전 자리에 있던 물고기를 임시 저장
                prev_fish = bowl[shark_next_c][shark_next_r]
                # 이전 상어의 방향도 임시 저장
                prev_dir = bowl[shark_now_c][shark_now_r][1]
                # 먹은 물고기 자리로 상어 이동 + 방향 바꾸기
                bowl[shark_next_c][shark_next_r] = (-1, bowl[shark_next_c][shark_next_r][1])
                # 지나간 자리는 빈 칸.
                bowl[shark_now_c][shark_now_r] = (0, 0)
                # 그리고 다음 이동을 진행
                ate += 1
                move_shark(bowl, current, ate)
                # 다녀오면 원상복구 해야지
                ate -= 1
                # 먹혔던 물고기는 부활하고
                bowl[shark_next_c][shark_next_r] = prev_fish
                # 상어도 다시 원래 자리로 돌아옴
                bowl[shark_now_c][shark_now_r] = (-1, prev_dir)
                # 물고기는 토해냄
                current -= bowl[shark_next_c][shark_next_r][0]
                
        # 다 탈출하고 오면 현재 경우의 답을 반환
    #print(max(current, answer))
    answer = max(current, answer)
    return answer

# 초기 답은 (0, 0)의 물고기 번호로 주고 진행.    
print(move_shark(original_bowl, answer, 1))