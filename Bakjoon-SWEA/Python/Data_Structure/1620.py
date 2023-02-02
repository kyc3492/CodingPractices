# 입력 최적화
import sys
input = sys.stdin.readline

# 0. 입력 세팅
N, M = map(int, input().split())

# 1. 이름 - 번호 순서의 테이블, 번호 - 이름 순서의 테이블 생성
poketdex_name_id = {}
poketdex_id_name = {}
for i in range(N):
    # 입력 최적화로 오버라이딩 한 경우 개행 문자를 없애줘야함
    name = input().rstrip()
    poketdex_name_id[name] = i + 1
    poketdex_id_name[i + 1] = name

# 2. 입력 구분해서 답 출력
for i in range(M):
    question = input().rstrip()
    if question.isnumeric():
        print(poketdex_id_name[int(question)])
    else:
        print(poketdex_name_id[question])