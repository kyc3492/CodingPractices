# 0. 입력 준비. BFS로 풀어보자
from collections import deque

n = int(input())
node = [0 for _ in range(n)]
k = int(input())
pairs = deque([])
for _ in range(k):
    c, r = map(int, input().split())
    pairs.append([c, r])
    
# 1. 쌍을 돌면서 1을 포함하는 쌍을 찾는다.
# 양방향 쌍이라는 것을 명심하고 찾은 후 BFS 큐에 넣는다.
queue = deque([])
for pair in pairs:
    if 1 in pair:
        queue.append(pair)

# 2. 큐를 돌린다.
while(queue):
    #print(queue)
    s, d = queue.popleft()
    node[s - 1] = 1
    node[d - 1] = 1
    # 다음 탐색지를 추가할 때 고려할 사항이 있는데,
    # 2-1. 다음 행선지로 가는 길이 있는가?
    for pair in pairs:
        if s in pair:
            # 2-2. 그렇게 찾은 길 중 방문하지 않았던 노드가 있는가?
            if node[pair[0] - 1] == 0 or node[pair[1] - 1] == 0:
                # 2-3. 혹시 이미 큐에 있진 않는가?
                if pair not in queue:
                    # 그렇다면 추가.
                    queue.append(pair)
        if d in pair:
            # 2-2. 그렇게 찾은 길 중 방문하지 않았던 노드가 있는가?
            if node[pair[0] - 1] == 0 or node[pair[1] - 1] == 0:
                # 2-3. 혹시 이미 큐에 있진 않는가?
                if pair not in queue:
                    # 그렇다면 추가.
                    queue.append(pair)

print(sum(node) - 1)