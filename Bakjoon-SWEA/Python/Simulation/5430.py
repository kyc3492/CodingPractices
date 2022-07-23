T = int(input())

for test_case in range(T):
    #print("Starting test ", test_case)
    p = str(input())
    n = int(input())
    arr = list(map(str, input().split(',')))
    Answer = ''
    isReversed = False

    #print(arr)
    arr[0] = arr[0][1:]
    #print(arr)
    arr[-1] = arr[-1][:-1]

    #print(n, arr)

    start = 0
    end = n - 1

    for c in p:
        if c == 'R':
            if isReversed == False:
                isReversed = True
                #print(c, end, start)
            else:
                isReversed = False
                #print(c, start, end)
        
        if c == 'D':
            if isReversed == False:
                start += 1
                #print(c, start, end)
            else:
                end -= 1
                #print(c, end, start)

    if start > end + 1:
            print("error")
            #print(start, end)
    elif start == end + 1:
            print("[]")
            #print(start, end)
    else:
        Answer += "["
        if isReversed == False:
            for i in range(start, end + 1):
                Answer += arr[i]
                if i != end:
                    Answer += ","
        else:
            for i in range(end, start - 1, -1):
                Answer += arr[i]
                if i != start:
                    Answer += ","
        Answer += "]"
        print(Answer)
        #print(start, end)
