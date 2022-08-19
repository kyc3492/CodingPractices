# 회전 방향이 주어지면 다른 톱니바퀴들의 회전방향 결정
# 각 톱니의 2, 6 톱니 확인

Gears = []
for _ in range(4):
    Gears.append(str(input()))
K = int(input())
Oper = []
for _ in range(K):
    Oper.append(list(map(int, input().split())))

#print(Gears)
#print(Oper)

def Rotate(g, d):
    if d == 1:
        tmp = Gears[g][7]
        Gears[g] = tmp + Gears[g][0:7]
    elif d == -1:
        tmp = Gears[g][0]
        Gears[g] = Gears[g][1:8] + tmp
    return

for g, d in Oper:
    AddedOper = [[g, d]]
    for i in range(1, 4):
        if 0 <= (g - 1) - i:
            if Gears[(g - 1) - i][2] != Gears[(g - 1) - (i - 1)][6]:
                #print("Can Rotate", g - i)
                if i % 2 == 1:
                    AddedOper.append([g - i, d * -1])
                else:
                    AddedOper.append([g - i, d])
            else:
                break
    for i in range(1, 4):
        if (g - 1) + i < 4:
            if Gears[(g - 1) + i][6] != Gears[(g - 1) + (i - 1)][2]:
                #print("Can Rotate", g + i)
                if i % 2 == 1:
                    AddedOper.append([g + i, d * -1])
                else:
                    AddedOper.append([g + i, d])
            else:
                break

    #print(AddedOper)
    for ng, nd in AddedOper:
        #print("Rotating...", ng, nd)
        Rotate(ng - 1, nd)

    #print("Finished Operation")

print(int(Gears[0][0]) + int(Gears[1][0]) * 2 + int(Gears[2][0]) * 4 + int(Gears[3][0]) * 8)