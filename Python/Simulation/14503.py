N, M = map(int, input().split())
R, C, D = map(int, input().split())
NR = 0
NC = 0
BR = 0
BC = 0
Room = []
for i in range(N):
    Room.append(list(map(int, input().split())))

def Direction_Selector(d):
    global D, NR, NC
    if d == 0:
        D = 3
        NR = R
        NC = C - 1
    elif d == 1:
        D = 0
        NR = R - 1
        NC = C
    elif d == 2:
        D = 1
        NR = R
        NC = C + 1
    else:
        D = 2
        NR = R + 1
        NC = C

def Direction_Backward(d):
    global BR, BC
    if d == 0:
        BR = R + 1
        BC = C
    elif d == 1:
        BR = R
        BC = C - 1
    elif d == 2:
        BR = R - 1
        BC = C
    else:
        BR = R
        BC = C + 1

Answer = 0
Counter = 0
while 1:
    '''청소하기'''
    if Room[R][C] == 0:
        Room[R][C] = -1
        Answer += 1
        Counter = 0

    '''왼쪽으로 회전'''
    Direction_Selector(D)
    '''빈 공간이면 이동'''
    if Room[NR][NC] == 0:
        R = NR
        C = NC
    else:
        '''아니면 회전만'''
        Counter += 1

    '''2a 4번 반복시'''
    if Counter == 4:
        '''후방 확인'''
        Direction_Backward(D)
        '''벽이면 작동 중지'''
        if Room[BR][BC] == 1:
            break
        else:
            '''아니면 뒤로 한 칸'''
            R = BR
            C = BC
            Counter = 0

print(Answer)