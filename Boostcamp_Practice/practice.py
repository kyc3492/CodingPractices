Arr = list(map(int, input().split()))
Answer = [-1]
MAX = max(Arr)

for n in range(1, MAX + 1):
    counter = 0
    for i in range(len(Arr)):
        if Arr[i] == n:
            counter += 1
    if counter > 1:
        if Answer[0] == -1:
            Answer.pop(0)
        Answer.append(counter)

print(Answer)