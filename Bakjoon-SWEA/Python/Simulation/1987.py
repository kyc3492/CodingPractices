R, C = map(int, input().split())
Board = []
for i in range(R):
    Board.append(input())

History = {}
dc = [-1, 0, 1, 0]
dr = [0, 1, 0, -1]

def Range_Checker(c, r):
    if 0 <= c < R and 0 <= r < C:
        return True
    else:
        return False

answer = 1
# 시간복잡도 해결 시도
alphas = set()

def DFS(c, r, cnt):
    global answer
    #print("Here is", c, r)
    for d in range(4):
        nc = c + dc[d]
        nr = r + dr[d]
        if Range_Checker(nc, nr):
            #if Board[nc][nr] not in History:
            if Board[nc][nr] not in alphas:
                #History[Board[nc][nr]] = 1
                alphas.add(Board[nc][nr])
                #print("Checking", nc, nr, Board[nc][nr])
                #print(History)
                DFS(nc, nr, cnt + 1)
                #del History[Board[nc][nr]]
                alphas.remove(Board[nc][nr])
            else:
                answer = max(answer, cnt)
    #return answer

#History[Board[0][0]] = 1
alphas.add(Board[0][0])
#DFS(0, 0, 1)

# 걍 맘 편하게 BFS로 갑시다...
def BFS(c, r):
    global answer
    queue = set([(c, r, Board[c][r])])
    while queue:
        c, r, ans = queue.pop()
        for d in range(4):
            nc = c + dc[d]
            nr = r + dr[d]
            if Range_Checker(nc, nr):
                if Board[nc][nr] not in ans:
                    queue.add((nc, nr, ans + Board[nc][nr]))
                    answer = max(answer, len(ans) + 1)
BFS(0, 0)
print(answer)