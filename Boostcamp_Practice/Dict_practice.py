Arr = list(map(int, input().split()))
Dict = {}
Answer = [-1]
MAX = max(Arr)

for i in range(MAX):
    Arr.count(i)
if counter > 1:
    if Answer[0] == -1:
        Answer.pop(0)
    Answer.append(counter)

print(Answer)