n, k = map(int, input().split())

josephus = [num for num in range(1, n + 1)]
taken = []

# 2초 넉넉하니까 pop 하자
idx = 0
while len(taken) < n:
    # 번째기 때문에 -1 해야됨.
    idx = (idx + (k - 1)) % len(josephus)
    taken.append(josephus.pop(idx))

answer = '<'
for t in taken:
    answer += str(t) + ', '
answer = answer[:-2] + '>'
print(answer)