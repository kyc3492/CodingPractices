import sys
sys.setrecursionlimit(10**6)

# 2. 지렁이 다니는 함수.
# 배추 있는 부분을 순회하며 돌면서 -1을 하고
# 0인 부분을 배추가 없는 부분 + 이미 다녀간 부분으로 치고 진행.
def warm(x, y):
    # 지렁이 다녀감.
    farm[x][y] -= 1
    # 사방으로 돌며 확인 진행
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 다음 좌표가 내부에 있다면 + 다음 좌표가 1이면
        if range_checker(nx, ny) and farm[nx][ny] == 1:
            # 다음 좌표로 재귀 진행.
            warm(nx, ny)

# 제시된 좌표가 범위 내에 있는지 체크        
def range_checker(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True
    else:
        return False

T = int(input())

for testcase in range(T):
    # 0. 입력 받기. M: 가로, N: 세로, K: 배추 총 개수
    M, N, K = map(int, input().split())
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 1. 빈 농장 세팅 + 입력 받는 위치에 배추 심기
    farm = [[0] * M for _ in range(N)]
    # c: 가로 위치(어떤 col?), r: 세로 위치(어떤 row?)
    # 2차원 배열에서는 서로 반대 위치임을 명심.
    for _ in range(K):
        col, row = map(int, input().split())
        farm[row][col] = 1
    
    answer = 0
    # 헷갈리니 차라리 col, row로 처리
    for col in range(M):
        for row in range(N):
            if farm[row][col] == 1:
                warm(row, col)
                # 3. 위의 논리대로 1일 때만 warm 함수를 진행한다면
                # 땅 덩어리를 만났을 때라는 뜻이므로 answer에 더해도 됨.
                answer += 1
    print(answer)