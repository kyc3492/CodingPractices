N, M = map(int, input().split())
count = 0
arr = []

def DFS():
    global count
    if count == M:
        for i in range(M):
            print(arr[i], end=" ")
        print()
    else:
        for i in range(1, N + 1):
            if i not in arr:
                arr.append(i)
                count += 1
                DFS()
                count -= 1
                arr.pop()

DFS()