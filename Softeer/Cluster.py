import sys

N, Budget = map(int, input().split())
#print(N, Budget)
Machines = list(map(int, input().split()))
#print(Machines)

Machines = sorted(Machines)
left = Machines[0]
right = 2000000000
Machines_dict = {}

for i in Machines:
    if i not in Machines_dict:
        Machines_dict[i] = 1
    else:
        Machines_dict[i] += 1

#print(Machines_dict)

while right - left > 1:
    mid = (right + left) // 2
    cost = 0
    isLeft = True
    #print("Now Mid", mid)

    for k, v in Machines_dict.items():
        if k < mid:
            cost += ((mid - k) ** 2) * v
            if cost > Budget:
                right = mid
                isLeft = False
                #print("Over Budget", cost, mid)
                break
    if isLeft == True:
        #print("Can Afford", cost, mid)
        left = mid

print(left)