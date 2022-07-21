T = str(input())
cnt = 0

idx = len(T) - 1
while 1:
    #print(T[idx])
    #print(idx)
    if idx < 0:
        break

    if T[idx] == '=' and idx > 0:
        idx -= 1
        if T[idx] == 'c' or T[idx] == 's':
            cnt += 1
            idx -= 1
        elif T[idx] == 'z':
            idx -= 1
            if T[idx] == 'd':
                cnt += 1
                idx -= 1
            else:
                cnt += 1
    elif T[idx] == '-' and idx > 0:
        idx -= 1
        if T[idx] == 'c' or T[idx] == 'd':
            cnt += 1
            idx -= 1
    elif T[idx] == 'j' and idx > 0:
        idx -= 1
        if T[idx] == 'l' or T[idx] == 'n':
            cnt += 1
            idx -= 1
        else:
            cnt += 1
    else:
        cnt += 1
        idx -= 1

print(cnt)