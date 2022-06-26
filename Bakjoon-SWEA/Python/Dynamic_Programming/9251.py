string1 = str(input())
string2 = str(input())

Memo = [[0] * (len(string1) + 1) for _ in range(len(string2) + 1)]

for i in range(1, len(string2) + 1):
    for j in range(1, len(string1) + 1):
        if string2[i - 1] == string1[j - 1]:
            Memo[i][j] = Memo[i - 1][j - 1] + 1
        else:
            Memo[i][j] = max(Memo[i - 1][j], Memo[i][j - 1])


print(Memo[len(string2)][len(string1)])