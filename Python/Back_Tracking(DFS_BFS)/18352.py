from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])
while q:
    print(q)
    now = q.popleft()
    #맨 앞에 뽑아(갈 수 있는 노드 중에서 가장 작은 숫자부터)
    print(now)
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)
            print(distance)

print(graph)
print(distance)