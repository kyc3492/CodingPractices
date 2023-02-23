import math

m = int(input())
n = int(input())

s = math.ceil(m ** 0.5)
powed = []
while (s * s) <= n:
    powed.append(s * s)
    s += 1

if len(powed) > 0:
    print(sum(powed))    
    print(powed[0])
else:
    print(-1)