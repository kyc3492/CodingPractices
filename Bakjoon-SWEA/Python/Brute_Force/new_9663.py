from sys import stdin

N = int(stdin.readline())
Answer = 0
Queens = [-1] * 15
#i -> 열, 원소 -> 행

#열과 대각선 체크
def Checker(index):
    for i in range(index):
        #print("Checking...", i, Queens[i], "...with...", index, Queens[index])
        if Queens[index] == Queens[i] or index - i == abs(Queens[index] - Queens[i]):
            return False
    
    #print("Profit")
    return True
            

def Nqueen(index):
    global Answer
    if index == N:
        #print("Final Profit")
        Answer += 1
        return

    #N번째 행까지 놓아보기
    for i in range(N):
        Queens[index] = i
        #print(Queens)
        if Checker(index) == True:
            #print("To the Next Index")
            Nqueen(index + 1)


Nqueen(0)
print(Answer)