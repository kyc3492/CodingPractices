T = int(input())
Answer = 0

for i in range(T):
    Text = str(input())
    Appear_List = []
    Checker = True
    
    index = 0
    while 1:
        if index < len(Text) and Text[index] not in Appear_List:
            Appear_List.append(Text[index])
            '''print("New Character Found on " + str(index) + Text[index])'''
            index += 1
        elif index > 0 and index < len(Text) and Text[index - 1] == Text[index]:
            '''print("Continues Character Found on " + str(index) + Text[index])'''
            index += 1
        elif index >= len(Text):
            '''print("End of Text " + str(index))'''
            break
        else:
            Checker = False
            '''print("Same Character Found on " + str(index) + Text[index])'''
            break

    if Checker == True:
        '''print("Rapid!")'''
        Answer += 1
    else:
        continue

print(Answer)