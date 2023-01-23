"""
# 0. 입력받기
n, m = map(int, input().split())

# 1. 입력 받으면서 해시 테이블 바로 생성
# 듣도 보도 못한 사람들을 전체적으로 확인해야하므로
# 두 명단 리스트를 통합해도 된다고 판단.
nohearsee = {}
for i in range(n + m):
    name = input()
    nohearsee[name] = nohearsee.setdefault(name, 0) + 1
    
# 2. 듣도보도 못한사람을 모두 뽑아보자.
# 각 명단에서 중복 인원은 없다고 했으므로
# 듣도 + 보도 못했다면 테이블에서 값은 2일 것.
answer = []
for name in nohearsee:
    if nohearsee[name] == 2:
        answer.append(name)

# 3. 알파벳 순 정렬 및 개수 출력
answer = sorted(answer)
print(len(answer))
for name in answer:
    print(name)
"""
# 시간 개선하기

# 0. 입력받기
n, m = map(int, input().split())

# 1. 입력 받으면서 해시 테이블 바로 생성
# 듣도 못한 사람들만 우선 확인한다.
nohear = {}
for i in range(n):
    name = input()
    nohear[name] = nohear.setdefault(name, 0) + 1
    
# 2. 듣도보도 못한사람을 모두 뽑아보자.
# 듣지 못한 사람들 중에서 보도 못한 사람을 키로 받아
# 존재한다면 듣도 + 보도 못한 사람이 되는 것.
answer = []
for i in range(m):
    name = input()
    if name in nohear:
        answer.append(name)

# 3. 알파벳 순 정렬 및 개수 출력
answer = sorted(answer)
print(len(answer))
for name in answer:
    print(name)