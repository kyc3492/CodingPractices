from collections import Counter
import sys

N = int(sys.stdin.readline())
El = []
sum = 0
for i in range(N):
    El.append(int(input()))
    sum += El[i]

print(round(sum / N))
print(sorted(El)[int(N / 2)])
cnt = Counter(El).most_common(N)
appear = []
if len(El) > 1:
    appear.append(cnt[0][0])
    for i in range(1, len(cnt)):
        if cnt[0][1] == cnt[i][1]:
            appear.append(cnt[i][0])
    if len(appear) > 1:
        print(sorted(appear)[1])
    else:
        print(sorted(appear)[0])
else:
    print(cnt[0][0])

print(sorted(El)[-1] - sorted(El)[0])