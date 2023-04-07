n, m, k, cont = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
killer = [[0] * n for _ in range(n)]

tree_directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
killer_directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

years = 0
answer = 0
while years < m:
    # 나무의 성장
    # 주변의 나무가 있는 칸 수를 구한 다음 더해주면 됨.
    for c in range(n):
        for r in range(n):
            if board[c][r] > 0:
                # 옆집에 나무가 있나?
                # 4방향
                for dc, dr in tree_directions:
                    nc = c + dc
                    nr = r + dr
                    # 범위 내라면
                    if 0 <= nc < n and 0 <= nr < n:
                        # 나무가 있는지 확인하고 그 지역 수만큼 더해줌
                        if board[nc][nr] > 0:
                            board[c][r] += 1

    # 중복 번식을 방지하기 위해 현 나무 정보들을 기억한다.
    prev_board = [[0] * n for _ in range(n)]
    for c in range(n):
        for r in range(n):
            prev_board[c][r] = board[c][r]

    # 나무의 번식
    # 주변에 아무것도 없는 칸 수를 구한 다음 나누어 분배.
    for c in range(n):
        for r in range(n):
            if prev_board[c][r] > 0:
                # 아무것도 없는 칸인가? + 제초제가 없는가? 에 해당하는 큐
                candi_list = []
                # 4방향
                for dc, dr in tree_directions:
                    nc = c + dc
                    nr = r + dr
                    # 범위 내라면
                    if 0 <= nc < n and 0 <= nr < n:
                        # 나무가 없는지 확인 + 제초제가 없다면
                        if prev_board[nc][nr] == 0 and killer[nc][nr] == 0:
                            candi_list.append((nc, nr))
                # 나누어야 할 나무 수 구하기
                # 동시 진행이기 때문에 더해준다.
                if candi_list:
                    tree = prev_board[c][r] // len(candi_list)
                    while candi_list:
                        candi_c, candi_r = candi_list.pop()
                        board[candi_c][candi_r] += tree

    can_kill = [[0] * n for _ in range(n)]

    # 제초제 성능 테스트
    best = (0, 0, 0)
    for c in range(n):
        for r in range(n):
            # 그 자리에 나무가 없다면 전파 ㄴㄴ
            if board[c][r] > 0:
                can_kill[c][r] = board[c][r]
                # 4방향 대각선으로 탐색을 k거리만큼 진행
                for dc, dr in killer_directions:
                    for dist in range(1, k + 1):
                        nc = c + (dc * dist)
                        nr = r + (dr * dist)
                        # 범위 내라면
                        if 0 <= nc < n and 0 <= nr < n:
                            # 나무가 아예 없거나 벽이 있다면 종료
                            if board[nc][nr] <= 0:
                                break
                            # 아니라면 박멸할 수 있는 나무로써 추가
                            else:
                                can_kill[c][r] += board[nc][nr]
                        else:
                            break
                # 성능이 제일 좋을 때를 찾는다.
                # 등호를 빼므로써 좌측, 상단에 우선순위를 둘 수 있다.
                if best[2] < can_kill[c][r]:
                    best = (c, r, can_kill[c][r])

    # 제초제를 뿌린다
    # 4방향 대각선으로 탐색을 k거리만큼 진행
    answer += best[2]
    killer[best[0]][best[1]] = cont + 1
    board[best[0]][best[1]] = 0
    for dc, dr in killer_directions:
        for dist in range(1, k + 1):
            nc = best[0] + (dc * dist)
            nr = best[1] + (dr * dist)
            # 범위 내라면
            if 0 <= nc < n and 0 <= nr < n:
                # 나무가 아예 없거나 벽이 있다면
                # 그 칸까지는 뿌려지고 종료
                # [매우 중요] 나무가 없더라도 제초제가 있다면 새로 뿌림
                # 제초제가 좀 남아있다면
                # 나무가 없거나 벽이면 거기까지만 뿌리고 전파 중지
                if board[nc][nr] <= 0:
                    killer[nc][nr] = cont + 1
                    break
                # 아니라면 박멸 진행
                else:
                    board[nc][nr] = 0
                    # 제초제를 +1 만큼 뿌린다. 그래야 마지막에 제초제 정리가 가능
                    killer[nc][nr] = cont + 1
            else:
                break

    # 제초제 1씩 감소
    for c in range(n):
        for r in range(n):
            if killer[c][r] > 0:
                killer[c][r] -= 1

    years += 1

print(answer)