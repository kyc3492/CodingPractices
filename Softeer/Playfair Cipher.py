import sys
# ord('A') = 65 / ort('Z') = 90

plain = input()
key = input()

board = [[0] * 5 for _ in range(5)]
history = {}

idx = 0
idx_alphabet = 65
for i in range(5):
    j = 0
    while j < 5:
        if idx < len(key):
            #print("Checking", key[idx], i, j)
            if key[idx] not in history:
                board[i][j] = key[idx]
                history[key[idx]] = 1
                idx += 1
                j += 1
            else:
                #print("Pass!!")
                idx += 1
        else:
            #print("Checking", chr(idx_alphabet), i, j)
            if chr(idx_alphabet) not in history and chr(idx_alphabet) != 'J':
                board[i][j] = chr(idx_alphabet)
                history[chr(idx_alphabet)] = 1
                idx_alphabet += 1
                j += 1
            else:
                #print("Pass!!")
                idx_alphabet += 1

#print(board)

idx = 0
chunk = []
while idx < len(plain):
    if idx == len(plain) - 1:
        if plain[idx] == 'X':
            chunk.append(plain[idx] + 'Q')
        else:
            chunk.append(plain[idx] + 'X')
        idx += 1
    elif plain[idx] == plain[idx + 1]:
        if plain[idx] == 'X':
            chunk.append(plain[idx] + 'Q')
        else:
            chunk.append(plain[idx] + 'X')
        idx += 1
    else:
        chunk.append(plain[idx] + plain[idx + 1])
        idx += 2

#print(chunk)

index_chunk = []
for c in chunk:
    tmp = []
    for k in range(2):
        for i in range(5):
            for j in range(5):
                if c[k] == board[i][j]:
                    #print(c[k], "is on", i, j)
                    tmp.append([i, j])
    #print(tmp)
    index_chunk.append(tmp)

answer = ''
for c in index_chunk:
    if c[0][0] == c[1][0]:
        #print("Same Row!")
        for i in range(2):
            if c[i][1] != 4:
                answer += board[c[i][0]][c[i][1] + 1]
            else:
                answer += board[c[i][0]][0]
    elif c[0][1] == c[1][1]:
        #print("Same Col!")
        for i in range(2):
            if c[i][0] != 4:
                answer += board[c[i][0] + 1][c[i][1]]
            else:
                answer += board[0][c[i][1]]
    else:
        #print("Other!")
        for i in range(2):
            if i == 0:
                answer += board[c[0][0]][c[1][1]]
            else:
                answer += board[c[1][0]][c[0][1]]

print(answer)