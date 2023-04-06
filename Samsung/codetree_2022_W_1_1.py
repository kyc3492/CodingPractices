# 입력 받기
n, m, k = map(int, input().split())
# 총 정보. 한 격자에 여러 개의 총이 놓일 수 있음에 유의
guns = [[[] for _ in range(n)] for _ in range(n)]
for c in range(n):
    tmp = list(map(int, input().split()))
    for r in range(n):
        guns[c][r].append(tmp[r])
# 플레이어 정보. [위치c, 위치r, 현 방향, 초기 능력치, 주운 총의 능력치]
# 위치 좌표는 +1 되어 있음에 유의하여 -1해서 넣어줄 거임.
# 또한 순서에 따라 idx를 부여. 1부터 할거임
players = {}
# 플레이어를 격자에 위치. 해당 위치에는 해당 idx가 오도록
board = [[0] * n for _ in range(n)]
for idx in range(1, m + 1):
    tmp = list(map(int, input().split()))
    tmp[0] -= 1
    tmp[1] -= 1
    tmp.append(0)
    board[tmp[0]][tmp[1]] = idx
    players[idx] = tuple(tmp)

# 바라보는 방향. 0~3까지
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
rounds = 0
points = [0 for _ in range(m + 1)]

# 라운드 진행하는 동안
while rounds < k:
    # 움직임을 구현할 거임. 분기 나누는 것에 주의
    for player_idx in range(1, m + 1):
        now_c, now_r, now_dir, now_att, now_gun = players[player_idx]
        # 바라보는 방향으로 이동할 수 있는지 확인. 만약 못 가면 뒤로돌아 가야함.
        nc = now_c + directions[now_dir][0]
        nr = now_r + directions[now_dir][1]
        if not (0 <= nc < n and 0 <= nr < n):
            nc = now_c + directions[(now_dir + 2) % 4][0]
            nr = now_r + directions[(now_dir + 2) % 4][1]
            # 방향 갱신.
            now_dir = (now_dir + 2) % 4
        
        # 이동했으므로 이전 위치는 빈 칸.
        board[now_c][now_r] = 0

        # 이동한 방향에 플레이어가 없다면
        if board[nc][nr] == 0:
            # 그런데 총은 있다면
            if guns[nc][nr]:
                # 플레이어가 총이 없었다면 획득
                if now_gun == 0:
                    # 바닥에 놓여진 총들 중 가장 높은 공격력의 것을 취함.
                    guns[nc][nr] = sorted(guns[nc][nr])
                    now_gun = guns[nc][nr].pop()
                # 플레이어가 이미 총이 있었다면
                else:
                    # 바닥에 놓여진 총들 중 가장 높은 공격력과 비교
                    if now_gun < sorted(guns[nc][nr])[-1]:
                        # 바닥 것이 더 높다면 내것을 놓고 바닥 것을 취함
                        guns[nc][nr].append(now_gun)
                        guns[nc][nr] = sorted(guns[nc][nr])
                        now_gun = guns[nc][nr].pop()
                    # 아나라면 넘어가면 됨.
            # 이 상황에서 현 플레이어의 상황을 업데이트
            players[player_idx] = (nc, nr, now_dir, now_att, now_gun)
            # 보드에도 업데이트
            board[nc][nr] = player_idx

        # 플레이어가 있다면
        else:
            # 전투 진행.
            # 현 상황에서의 플레이어의 바뀐 위치를 반영
            players[player_idx] = (nc, nr, now_dir, now_att, now_gun)
            # 상대방을 보드에서 일단 지운다.
            oppo_idx = board[nc][nr]
            board[nc][nr] = 0
            # 총 + 기본 능력치가 더 높은 사람이 포인트를 취함.
            match_point = (now_gun + now_att) - (players[oppo_idx][3] + players[oppo_idx][4])
            # 승자 기록. 초기 능력치 승부로 갔을 때 총기 선택권을 주기 위해서임.
            # 패자 역시 이동을 위해 기록해둠.
            winner = 0
            loser = 0
            # 현재 라운드의 플레이어가 이겼다면
            if match_point > 0:
                # 현재 플레이어의 포인트가 전체 공격력 차이만큼 획득
                winner = player_idx
                loser = oppo_idx
            # 졌다면
            elif match_point < 0:
                winner = oppo_idx
                loser = player_idx
            # 비겼다면 기초 능력치를 비교해야함.
            else:
                att_match_point = now_att - players[oppo_idx][3]
                # 기초 능력치를 비교. 같은 능력치를 주는 경우는 없음.
                # 현재 라운드의 플레이어가 이겼다면
                if att_match_point > 0:
                    # 현재 플레이어의 포인트가 전체 공격력 차이만큼 획득
                    winner = player_idx
                    loser = oppo_idx
                # 졌다면
                elif att_match_point < 0:
                    winner = oppo_idx
                    loser = player_idx

            # 포인트 지급. 능력치 승부까지 갔다면 0일 수도 있다.
            points[winner] += abs(match_point)

            # 패자 도망
            # 패자의 정보를 가져온다.
            loser_c, loser_r, loser_dir, loser_att, loser_gun = players[loser]
            # 보드에서 일단 지우고
            board[loser_c][loser_r] = 0
            # 현재 격자에 총을 내려놓는다.
            guns[loser_c][loser_r].append(loser_gun)
            loser_gun = 0
            loser_nc = 0
            loser_nr = 0
            # 가지고 있는 방향으로 나아가는데 90도씩 회전하므로
            for dir_idx in range(4):
                loser_nc = loser_c + directions[(loser_dir + dir_idx) % 4][0]
                loser_nr = loser_r + directions[(loser_dir + dir_idx) % 4][1]
                # 범위 내인가?
                if 0 <= loser_nc < n and 0 <= loser_nr < n:
                    # 플레이어가 없는가?
                    if board[loser_nc][loser_nr] == 0:
                        # 이동한 방향을 기록.
                        loser_dir = (loser_dir + dir_idx) % 4
                        # 해당 칸에 총이 있다면?
                        if guns[loser_nc][loser_nr]:
                            # 이동해서 총을 취한다.
                            guns[loser_nc][loser_nr] = sorted(guns[loser_nc][loser_nr])
                            loser_gun = guns[loser_nc][loser_nr].pop()
                        break
            # 현재 패자의 정보를 업데이트
            players[loser] = (loser_nc, loser_nr, loser_dir, loser_att, loser_gun)
            # 보드에도 업데이트
            board[loser_nc][loser_nr] = loser

            # 승자 재정비. 현재 위치에서 최강의 총을 취함.
            winner_c, winner_r, winner_dir, winner_att, winner_gun = players[winner]
            # 현재 총이 바닥의 제일 좋은 총보다 구리다면
            if winner_gun < sorted(guns[winner_c][winner_r])[-1]:
                # 내 총을 놓고 최강 총을 먹는다.
                guns[winner_c][winner_r].append(winner_gun)
                guns[winner_c][winner_r] = sorted(guns[winner_c][winner_r])
                winner_gun = guns[winner_c][winner_r].pop()
            # 현재 승자의 정보를 업데이트
            players[winner] = (winner_c, winner_r, winner_dir, winner_att, winner_gun)
            # 보드에도 업데이트
            board[winner_c][winner_r] = winner

    rounds += 1

# 포인트 출력
for p_idx in range(1, m + 1):
    print(points[p_idx], end=" ")