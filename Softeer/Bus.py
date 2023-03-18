import sys
input = sys.stdin.readline

n = int(input())
bus = list(map(int, input().split()))
arr = [[0 for i in range(n + 1)] for j in range(n + 1)]

for j in range(n - 1, -1, -1):
    for x in range(1, n + 1):
        if bus[j] < x:
            arr[x][j] = arr[x][j + 1] + 1
            # arr[X][j]는 j 번째 보다 오른쪽에 있는 버스들 중, x 보다 값이 작은 것들의 개수
        else:
            arr[x][j] = arr[x][j + 1]

ans = 0
for i in range(n):
    for j in range(i, n):
        if bus[i] < bus[j]:
            ans += arr[bus[i]][j]

print(ans)
