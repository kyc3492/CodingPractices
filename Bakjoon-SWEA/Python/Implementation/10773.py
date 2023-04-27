k = int(input())

# 맨 마지막 수를 지우므로 stack
stack = []
for _ in range(k):
    now = int(input())
    if now == 0:
        stack.pop()
    # 지울 원소가 항상 있음을 보장하므로
    else:
        stack.append(now)

print(sum(stack))