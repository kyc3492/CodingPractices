# https://school.programmers.co.kr/learn/courses/30/lessons/120921?language=python3
# 문자열 밀기. deque로 풀면 더 빠를듯?

def rotate_right(A, B):
    cnt = 0
    A = list(A)
    B = list(B)
    while (A != B):
        if cnt == len(A):
            break
        tmp = A[-1]
        tmp_list = list(A[0:-1])
        A = []
        A.append(tmp)
        A.extend(tmp_list)
        cnt += 1
        print(A, cnt)
    return cnt
    
def rotate_left(A, B):
    cnt = 0
    A = list(A)
    B = list(B)
    while (A != B or cnt < len(A)):
        if cnt == len(A):
            break
        tmp = A[0]
        A = list(A[1:])
        A.append(tmp)
        cnt += 1
        print(A, cnt)
    return cnt

def solution(A, B):
    answer = 0
    
    cnt_right = rotate_right(A, B)
    cnt_left = rotate_left(A, B)
    answer = min(cnt_right, cnt_left)
    if answer == len(A):
        answer = -1
    
    return answer