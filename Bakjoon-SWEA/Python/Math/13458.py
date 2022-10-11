N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0
for a in A:
    a -= B
    answer += 1

    if a > 0:
        if a % C:
            #print("Need 1 more")
            #print(a, B, C)
            answer += (a // C) + 1
        else:
            #print(a, B, C)
            answer += (a // C)

print(answer)