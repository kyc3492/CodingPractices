# 문제 조건이었음
MAX_N = 100000
MAX_M = 100000

# 변수 미리 선언
n, m, q = -1, -1, -1

# id에 해당하는 상자의 이전을 나타내는 prev와 다음을 나타내는 next를 관리한다. 0이면 없다는 뜻
# 이를 통해 링크드리스트의 역할을 구현한다.
prev = [0] * (MAX_M + 1)
next = [0] * (MAX_M + 1)

# 각 벨트별로 필요한 변수를 관리한다. 0이면 없다는 뜻
# head -> 맨 앞, tail -> 맨 뒤, num_gift -> 총 선물 개수
head = [0] * MAX_N
tail = [0] * MAX_N
num_gift = [0] * MAX_N

# 공장 생성 함수
def initialize_factory(op):
    n = op[1]
    m = op[2]

    # 벨트 정보 생성
    belts = [[] for _ in range(n)]
    for idx in range(1, m + 1):
        # op[3] 부터 op[3 + m]까지는 op[idx + 2] - 1 번 벨트에 넣을 박스를 주어짐.
        # 박스 번호를 1부터 주어가며 각 벨트에 배분할 거임.
        box_num = op[idx + 2] - 1
        # idx는 1부터 m + 1까지 순차로 증가하니까 박스 번호를 대변할 수 있음.
        belts[box_num].append(idx)

    # 생성된 벨트들을 idx로 돌면서 head, tail, prev, next 설정
    for idx in range(n):
        # 벨트가 비어있다면 패스
        if len(belts[idx]) == 0:
            continue

        # head -> 맨 앞 / tail -> 맨 뒤
        head[idx] = belts[idx][0]
        tail[idx] = belts[idx][-1]

        # num_gifts[idx] -> 해당 벨트 내 총 선물 개수
        num_gift[idx] = len(belts[idx])

        # prev -> 각 박스의 이전 박스 / next -> 각 박스의 이후 박스
        # 박스 번호를 1부터 주었기에 0은 없는 것
        for box_idx in range(len(belts[idx]) - 1):
            prev[belts[idx][box_idx + 1]] = belts[idx][box_idx]
            next[belts[idx][box_idx]] = belts[idx][box_idx + 1]

# 물건을 전부 옮긴다
def move_all(op):
    # 물건이 올 벨트와 갈 벨트를 받는다.
    src = op[1] - 1
    dest = op[2] - 1

    # src에 물건이 없으면 dest는 그대로
    if num_gift[src] == 0:
        print(num_gift[dest])
        return

    # dest에 물건이 없었던 상태라면 src에서 그대로 가져가면 된다.
    # 놀랍게도 head와 tail만 변경해주면 된다.
    # 어짜피 prev, next 관계는 그대로 유지되기 때문
    if num_gift[dest] == 0:
        head[dest] = head[src]
        tail[dest] = tail[src]
    # 아니라면 dest 앞으로 src 박스를 가져와야함
    else:
        # dest의 head를 dest의 tail + 1로 이동하는데 이는 prev와 next를 고치면 된다.
        # src의 tail 다음에는 dest의 head가 온다.
        next[tail[src]] = head[dest]
        # 이를 역으로 말하면 dest의 head 이전에는 src의 tail이 온다.
        prev[head[dest]] = tail[src]
        # head는 src의 것으로 변경, dest의 tail은 유지
        head[dest] = head[src]

    # src는 이제 비어있으므로
    head[src] = 0
    tail[src] = 0

    # 상자 개수 갱신
    num_gift[dest] += num_gift[src]
    num_gift[src] = 0

    print(num_gift[dest])


# head 제거
def pop_head(idx):
    # 벨트가 비어있다면 패스
    global  num_gift
    if num_gift[idx] == 0:
        return 0

    # 이제 해당 벨트에서의 head를 반환해야하는데
    idx_head = 0
    # 만약 박스가 1개밖에 없다면 head, tail을 전부 삭제
    # 벨트 내 박스 개수도 0
    if num_gift[idx] == 1:
        idx_head = head[idx]
        head[idx] = 0
        tail[idx] = 0
        num_gift[idx] = 0
    # 아니라면 head를 다음번째로 넘겨줄 필요가 있음
    else:
        idx_head = head[idx]
        head[idx] = next[idx_head]
        # 넘겨 받았다면 직전 두번째였던 박스에서는 prev가 없어야한다.
        prev[head[idx]] = 0
        # 마찬가지로 직전 head의 next도 없어짐
        next[idx_head] = 0
        # 박스 개수는 -1
        num_gift[idx] -= 1

    return idx_head


# 입력 받은 head를 맨 앞에 추가
def push_head(belt_idx, new_head):
    # 받은 head가 0이라면 진행 불가
    if new_head == 0:
        return 0

    # 원래 비어있었다면
    if not num_gift[belt_idx]:
        # head와 tail이 함께 추가됨.
        head[belt_idx] = new_head
        tail[belt_idx] = new_head
        num_gift[belt_idx] += 1
    # 아니라면
    else:
        # head만 추가됨. next와 prev 관계 재정립에 주의
        # 원래 head
        ori_head = head[belt_idx]
        next[new_head] = ori_head
        prev[ori_head] = new_head
        head[belt_idx] = new_head
        num_gift[belt_idx] += 1


# 앞 물건만 교체한다.
def swap_head(op):
    # src와 dest 초기화
    src, dest = op[1] - 1, op[2] - 1

    # head를 pop하는 함수와 push하는 함수를 만들어 활용
    src_head = pop_head(src)
    dest_head = pop_head(dest)
    push_head(dest, src_head)
    push_head(src, dest_head)

    print(num_gift[dest])

# 물건 나눠 옮기기
def divide_products(op):
    src, dest = op[1] - 1, op[2] - 1

    # 순서대로 박스를 뺀다.
    # 박스개수 // 2를 활용한다. 1 // 2는 0이므로 1개인 경우에 옮기지 않는 조건이 충족된다.
    gift_stack = []
    for idx in range(num_gift[src] // 2):
        gift_stack.append(pop_head(src))
        # 결국 하나하나 head를 빼는 것과 동일하다.

    # 거꾸로 넣어준다.
    for idx in range(len(gift_stack) - 1, -1, -1):
        # 결국 하나하나 head를 밀어넣어주는 것과 동일하다.
        push_head(dest, gift_stack[idx])

    print(num_gift[dest])


def gift_info(op):
    p_num = op[1]

    a = prev[p_num] if prev[p_num] != 0 else -1
    b = next[p_num] if next[p_num] != 0 else -1

    print(a + 2 * b)

def belt_info(op):
    b_num = op[1] - 1

    a = head[b_num] if head[b_num] != 0 else -1
    b = tail[b_num] if tail[b_num] != 0 else -1
    c = num_gift[b_num]

    print(a + 2 * b + 3 * c)

# 명령 입력 단계
q = int(input())
for idx in range(q):
    op = list(map(int, input().split()))
    if op[0] == 100:
        initialize_factory(op)
    elif op[0] == 200:
        move_all(op)
    elif op[0] == 300:
        swap_head(op)
    elif op[0] == 400:
        divide_products(op)
    elif op[0] == 500:
        gift_info(op)
    elif op[0] == 600:
        belt_info(op)