N = int(input())
Answer = 0

def Checker(N):
    N_str = str(N)
    tmp = []
    for i in N_str:
        tmp.append(i)
    if len(tmp) < 3:
        return True
    else:
        interval = int(N_str[1]) - int(N_str[0])
        for c in range(1, len(N_str) - 1):
            if int(N_str[c + 1]) - int(N_str[c]) != interval:
                return False
            else:
                return True

for i in range(1, N + 1):
    if Checker(i) == True:
        Answer += 1

print(Answer)