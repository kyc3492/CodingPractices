#https://programmers.co.kr/learn/courses/30/lessons/72410
#신규 아이디 추천
#정규식? 보다는 꼼꼼하게 보기. 문자열 마스터

def solution(new_id):
    answer = ''
    
    #1단계
    answer1 = new_id.lower()
    
    #2단계
    answer2 = ''
    for c in answer1:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer2 += c
    #print("2: ", answer2)
    
    #3단계
    answer3 = ''
    while '..' in answer2:
        answer2 = answer2.replace('..', '.')
    answer3 = answer2
    #print("3: ", answer3)
    
    #4단계
    answer4 = ''
    if answer3[0] == '.':
        answer3 = answer3[1:] if len(answer3) > 1 else '.'
    if answer3[-1] == '.':
        answer3 = answer3[:-1]
    answer4 = answer3
    #print("4: ", answer4)
    
    #5단계
    if answer4 == '':
        answer4 = 'a'
    answer5 = answer4
    
    #6단계
    while len(answer5) >= 16:
        answer5 = answer5[:-1]
    if answer5[-1] == '.':
        answer5 = answer5[:-1]
    answer6 = answer5
    
    #7단계
    while len(answer6) <= 2:
        answer6 += answer6[-1]
    answer = answer6
    
    return answer