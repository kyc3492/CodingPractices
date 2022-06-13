N = int(input())
Tri = []
for _ in range(N):
    Tri.append(list(map(int, input().split())))

for i in range(N - 1, 0, -1):
    if i - 1 >= 0:
        for j in range(i):
            Tri[i - 1][j] = max(Tri[i - 1][j] + Tri[i][j], Tri[i - 1][j] + Tri[i][j + 1])

print(Tri[0][0])