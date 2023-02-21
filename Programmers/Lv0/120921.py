# https://school.programmers.co.kr/learn/courses/30/lessons/120921?language=python3
# 문자열 밀기. deque로 풀면 더 빠를듯?

from collections import deque

def rotate_right(A, B):
    cnt = 0
    A = deque(A)
    B = deque(B)
    while (A != B):
        if cnt == len(A):
            break
        tmp = A.pop()
        A.appendleft(tmp)
        cnt += 1
        print(A, cnt)
    return cnt

def solution(A, B):
    answer = rotate_right(A, B)
    if answer == len(A):
        answer = -1
    
    return answer