N = int(input())
ans = abs(100 - N)
M = int(input())
Notwork = []
if M != 0:
    Notwork = list(map(int, input().split()))
Canmake = True

for num in range(1000001):
    for i in str(num):
        if int(i) in Notwork:
            Canmake  = False
            break
    if Canmake == True:
        ans = min(ans, len(str(num)) + abs(int(num) - N))
    Canmake = True

print(ans)