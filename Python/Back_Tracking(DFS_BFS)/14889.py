from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
Roaster = []
for i in range(N):
    Roaster.append(list(map(int, input().split())))
Each = int(N/2)
Team1 = set([])
count = 0
Seleted = [False] * N
Balance = 100

def Team(index):
    global count, Team1, Team2, Balance

    if count == Each:
        Team1_sum = 0
        Team2_sum = 0
        Team2 = All_Players - Team1

        #중복계산을 방지하기 위해 조합 함수 사용
        for i, j in combinations(Team1, 2):
            Team1_sum += Roaster[i][j] + Roaster[j][i]
        for i, j in combinations(Team2, 2):
            Team2_sum += Roaster[i][j] + Roaster[j][i]

        #print("Checking with Team1: ", Team1, "/ Team2: ", Team2)
        #print("Checking balance...", Team1_sum, Team2_sum)

        Balance = min(Balance, abs(Team1_sum - Team2_sum))

    else:
        for i in range(index, N):
            if Seleted[i] == False:
                #print("picked up... ", i)
                Team1.add(i)
                Seleted[i] = True
                count += 1
                Team(i + 1)
                count -= 1
                Seleted[i] = False
                #print("put down... ", i)
                Team1.remove(i)    

All_Players = set(i for i in range(N))
Team(0)
#print("Checking with Team1: ", Team1, "/ Team2: ", Team2)
print(Balance)