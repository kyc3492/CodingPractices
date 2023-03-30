# DFS를 스택으로 구현하는 것을 연습하자.
# BFS가 정석이긴 한데 ㅎ
# 입력받기
n, m = map(int, input().split())
miro = [list(input()) for _ in range(n)]

# 거리 기록용 리스트
dist = [[0] * m for _ in range(n)]
dist[0][0] = 1

# 미로를 돌 건데 DFS로 돌거임.
# 스택으로 DFS를 구현해보자.
# 위치 + 현재 간 수를 스택으로 밀어버릴거임.
stack = [(0, 0)]
answer = n * m

while stack:
    c, r = stack.pop()
    
    # 현재 위치가 목적지라면 answer에 반영
    if (c + 1) == n and (r + 1) == m:
        answer = min(answer, dist[c][r])

    # 사방으로 확인
    for dc, dr in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nc = c + dc
        nr = r + dr
        # 범위 내에 있고
        if 0 <= nc < n and 0 <= nr < m:
            # 다음 행선지에 갈 수 있을 때 + 간 적이 없거나 여기서 가는게 더 빠르다면
            if miro[nc][nr] == '1':
                if dist[nc][nr] == 0 or dist[nc][nr] > dist[c][r] + 1:
                    # 다음 행선지까지 기록된 거리를 확인하는데
                    # 이 거리가 지금에서 추가되는 거리보다 짧다면 갱신
                    dist[nc][nr] = dist[c][r] + 1
                    # 스택에 추가해준다.
                    stack.append((nc, nr))
                
                
print(answer)