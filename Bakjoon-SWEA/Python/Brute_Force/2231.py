# 0. 입력 받기
n = int(input())
answer = 0

# 1. 부르트 포스이므로 1부터 그냥 돌려버려도 될 듯.
# 단, 제일 작은 생성자를 찾으라 했고 분해합 특성 상 n보다는 작아야 함.
for number in range(1, n + 1):
    # 1-1. int -> str -> 각 자리수 list로 변환
    number_listed = list(str(number))
    # 1-2. 각 자리수 list를 int로 다시 바꿔서 진행
    number_listed = [int(i) for i in number_listed]
    
    # 2. 생성자인지 체크
    if number + sum(number_listed) == n:
        answer = number
        break
    
print(answer)