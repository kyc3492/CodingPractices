N = int(input())
Arr = list(map(int, input().split()))
Arr_sum = [0] * N
Arr_sum[0] = Arr[0]

for i in range(1, N):
    Arr_sum[i] = max(Arr[i], Arr_sum[i - 1] + Arr[i])

print(max(Arr_sum))