from collections import deque
n, k = map(int, input().split())

divider = deque([])
divider_right = deque([])
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        #print(i, int(n / i))
        divider.append(i)
        if i != int(n / i):
            divider_right.appendleft(int(n / i))
divider.extend(divider_right)
#print(divider)

if len(divider) >= k:
    print(divider[k - 1])
else:
    print(0)

"""
n, k = map(int, input().split())

divider = []
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        #print(i, int(n / i))
        divider.append(i)
        if i != int(n / i):
            divider.append(int(n / i))
divider = sorted(divider)
#print(divider)

if len(divider) >= k:
    print(divider[k - 1])
else:
    print(0)
"""