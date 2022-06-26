L, C = map(int, input().split())
Letters = sorted(list(map(str, input().split())))
Password = []
count = 0

def DFS(index):
    global Password, count
    if count == L:
        Vowel_check = 0
        Cons_check = 0

        for c in Password:
            if c in ['a', 'e', 'i', 'o', 'u']:
                Vowel_check += 1
            else:
                Cons_check += 1

        if Vowel_check >= 1 and Cons_check >=2:
            for c in Password:
                print(c, end="")
            print()
    
    else:
        for i in range(index, C):
            Password.append(Letters[i])
            count += 1
            DFS(i + 1)
            count -= 1
            Password.pop()

#print(Letters)
DFS(0)