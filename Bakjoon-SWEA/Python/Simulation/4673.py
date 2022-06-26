def Self_Maker(N):
    tmp = []
    for i in str(N):
        tmp.append(i)
    for i in tmp:
        N += int(i)
    return N

Arr = [0] * 10000
for i in range(10000):
    tmp = Self_Maker(i)
    if tmp < 10000:
        Arr[tmp] = 1

for i in range(10000):
    if Arr[i] == 0:
        print(i)