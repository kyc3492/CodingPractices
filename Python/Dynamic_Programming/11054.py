N = int(input())
Data = []
Data = list(map(int, input().split()))

Memo_Inc = [1] * N
Memo_Dec = [1] * N
Memo_All = [0] * N

for k in range(N):
    for i in range(k):
        if Data[i] < Data[k]:
            Memo_Inc[k] = max(Memo_Inc[k], Memo_Inc[i] + 1)
        if Data[len(Data) - i - 1] < Data[len(Data) - k - 1]:
            Memo_Dec[len(Data) - k - 1] = max(Memo_Dec[len(Data) - k - 1], Memo_Dec[len(Data) - i - 1] + 1)

for i in range(N):
    Memo_All[i] = Memo_Inc[i] + Memo_Dec[i] - 1

print(sorted(Memo_All)[-1])