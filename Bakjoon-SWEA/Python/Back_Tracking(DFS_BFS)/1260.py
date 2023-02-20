# 0. BFS 구현을 위한 deque 세팅
from collections import deque

# 입력 받기
n, m, v = map(int, input().split())
board = [[0] * n for _ in range(n)]
# 지도 구성 (경로 유무)
for _ in range(m):
    s, d = map(int, input().split())
    board[s - 1][d - 1] = 1
    board[d - 1][s - 1] = 1


# 1. DFS 구현. 재귀로 구현한다.
def DFS(s):
    result_dfs.append(s + 1)
    # 갈 수 있는 노드 리스트 확인
    node_list = []
    for idx in range(n):
        if board[s][idx] == 1:
            node_list.append(idx)
            
    for next in node_list:
        # 방문한 곳이 아니라면
        if next + 1 not in result_dfs:
            DFS(next)
            
            
# 2. BFS 구현. 큐로 구현한다.
def BFS(s):
    node_list = deque([s])
                 
    while(node_list):
        next = node_list.popleft()
        
        # 갈 수 있는 노드 리스트 확인
        # 그 중에 방문한 곳이 아닌지를 확인해야 함.
        for idx in range(n):
            if board[next][idx] == 1 and idx + 1 not in result_bfs:
                node_list.append(idx)

        # 방문 기록에 넣을 때에도 겹치지 않는지 확인.
        if next + 1 not in result_bfs:
            result_bfs.append(next + 1)
            
            

result_dfs = []
DFS(v - 1)

result_bfs = []
BFS(v - 1)

for n in result_dfs:
    print(n, end=" ")
print()
for n in result_bfs:
    print(n, end=" ")