from collections import defaultdict

# 초기 값 지정
n, m = -1, -1
MAX_N, MAX_M = 100000, 10
# 이중 연결리스트의 초기화 -> head, tail, total, prev, next
# 벨트는 최대 10개, idx대로 1~10
head = [0 for _ in range(MAX_M + 1)]
tail = [0 for _ in range(MAX_M + 1)]
# 물건은 ID: Weight 모양의 dict를 만들자.
weight = defaultdict(lambda : 0)
# prev, next 역시 dict를 만들면 된다.
# lambda 식으로 defaultdict를 만들어주면 순회 돌면서 찾는 속도를 줄일 수 있음.
prev = defaultdict(lambda: 0)
next = defaultdict(lambda: 0)

broken = [False] * MAX_M
# 물건 id 별 벨트 번호를 기록할 것임.
# -1은 사라진 물건.
belt_num = defaultdict(lambda: -1)

# 공장 설립
def build_factory(command):
    global n, m
    n, m = command[1], command[2]

    # id들과 무게들을 받아옴.
    box_ids = [command[idx] for idx in range(3, n + 3)]
    box_weights = [command[idx] for idx in range(n + 3, 2 * n + 3)]

    # 한 벨트당 넣을 수 있는 박스 개수 초기화
    MAX_SIZE = n // m

    idx = 0
    while idx < n:
        # 한 벨트에 최대 사이즈까지
        for belt_idx in range(1, m + 1):
            # 벨트의 head와 tail을 지정
            head[belt_idx] = box_ids[idx]
            tail[belt_idx] = box_ids[idx + (MAX_SIZE - 1)]
            # MAX 사이즈까지 돌면서 넣자
            for size in range(MAX_SIZE):
                # 무게 넣어주고
                weight[box_ids[idx]] = box_weights[idx]
                # 벨트 넘버 할당
                # +1 해서 넣어줌에 주의
                belt_num[box_ids[idx]] = belt_idx
                # tail이 아니라면 관계정립 가능
                if size < MAX_SIZE - 1:
                    prev[box_ids[idx + 1]] = box_ids[idx]
                    next[box_ids[idx]] = box_ids[idx + 1]
                idx += 1

    return

# 받은 idx의 벨트에서 head를 넘겨주고 이전 head를 반환해주는 함수
def pop_head(belt_idx):
    # 현재 head를 받아둠.
    ori_head = head[belt_idx]
    # 다음 head
    next_head = next[ori_head]
    # 현재 head의 next / 다음 head의 prev, next 관계 청산
    next[ori_head] = 0
    prev[next_head] = 0
    # head 변경
    head[belt_idx] = next_head
    # 이전 head 반환
    return ori_head

# 받은 idx의 벨트에 id 박스를 꼬리로써 추가해주는 함수
def push_tail(belt_idx, box_id):
    # 현재 tail을 받아둠.
    ori_tail = tail[belt_idx]
    # 현재 tail 다음으로 올 다음 tail과의 prev, next 관계를 생성
    next[ori_tail] = box_id
    prev[box_id] = ori_tail
    # tail 변경
    tail[belt_idx] = box_id
    return


# 상자 하차
def load_boxes(command):
    w_max = command[1]
    loaded = 0

    # 컨베이어벨트들을 확인
    for belt_idx in range(1, m + 1):
        # 고장난 건 패스
        if broken[belt_idx] == -1:
            continue
        # 각 벨트들의 head를 본다
        # 이 head가 w_max 이하라면
        if weight[head[belt_idx]] <= w_max:
            # 하차 무게에 더하고
            loaded += weight[head[belt_idx]]
            # head를 넘겨줘야함. + 해당 벨트에서 내리자
            loading = pop_head(belt_idx)
            belt_num[loading] = -1
            # weight도 0으로 만들어 삭제해준다.
            weight[loading] = 0
        else:
            # head를 받아서 tail로 변경해주는 것과 같음.
            push_tail(belt_idx, pop_head(belt_idx))

    print(loaded)
    return

# 상자 제거
def remove_box(command):
    r_id = command[1]

    if belt_num[r_id] == -1:
        print(-1)
        return

    # 해당 박스의 소속 벨트를 확인한다.
    b_num = belt_num[r_id]
    # 삭제할 거니까 소속 벨트 정보는 삭제
    belt_num[r_id] = -1

    # 분기 처리
    # 하나 있던 거라면
    if head[b_num] == tail[b_num]:
        # head, tail만 삭제
        head[b_num] = 0
        tail[b_num] = 0
    # head를 삭제한다면
    elif r_id == head[b_num]:
        # head 변경
        next_id = next[r_id]
        head[b_num] = next_id
        # 땡겨진 head의 prev 삭제
        prev[next_id] = 0
    # tail을 삭제한다면
    elif r_id == tail[b_num]:
        # tail 삭제
        prev_id = prev[r_id]
        tail[b_num] = prev_id
        next[prev_id] = 0
    # 중간에 있는 거라면 prev, next만 수정
    else:
        prev_id = prev[r_id]
        next_id = next[r_id]
        prev[next_id] = prev_id
        next[prev_id] = next_id

    next[r_id] = 0
    prev[r_id] = 0

    print(r_id)
    return



# 상자 찾아 그 상자에서부터 tail까지 다 가져오기
def find_box(command):
    f_id = command[1]
    # 이미 없는 상자인지 확인
    if belt_num[f_id] == -1:
        print(-1)
        return

    b_num = belt_num[f_id]

    # 해당 상자가 이미 head가 아닐 때에만 적용
    if head[b_num] != f_id:
        # head, tail 변경
        ori_head = head[b_num]
        ori_tail = tail[b_num]
        # 해당상자 이후 상자들을 모두 가져와야하므로
        # 직전 상자를 받아둔다.
        prev_id = prev[f_id]

        head[b_num] = f_id
        tail[b_num] = prev_id
        prev[ori_head] = ori_tail
        next[ori_tail] = ori_head

        prev[f_id] = 0
        next[prev_id] = 0

    print(b_num)


# 벨트의 고장
def bad_belt(command):
    b_num = command[1]

    # 이미 고장난 컨베이어벨트면 -1 출력
    if broken[b_num] == True:
        print(-1)
        return

    broken[b_num] = True

    # 빈 벨트라면 패스
    if head[b_num] == 0:
        print(b_num)
        return

    isFinished = False

    # 컨베이어벨트들을 확인
    # 현제 벨트에서부터 바로 오른쪽부터 확인
    belt_idx = b_num
    while 1:
        belt_idx = (belt_idx + 1) % m

        # 망가지지 않은 곳이라면
        if not broken[belt_idx]:
            # 비어있다면 그대로 옮겨주면 됨.
            if tail[belt_idx] == 0:
                head[belt_idx] = head[b_num]
                tail[belt_idx] = tail[b_num]
            else:
                # 해당 위치로 상자를 전부 옮긴다.
                wanna_move = pop_head(b_num)
                push_tail(belt_idx, wanna_move)
                belt_num[wanna_move] = belt_idx

            # 전체 벨트 위치 갱신
            box_idx = head[b_num]
            while box_idx != 0:
                belt_num[box_idx] = belt_idx
                box_idx = next[box_idx]

            head[b_num] = tail[b_num] = 0
            break

    print(b_num)
    return


q = int(input())
for _ in range(q):
    command = list(map(int, input().split()))
    if command[0] == 100:
        build_factory(command)
    elif command[0] == 200:
        load_boxes(command)
    elif command[0] == 300:
        remove_box(command)
    elif command[0] == 400:
        find_box(command)
    elif command[0] == 500:
        bad_belt(command)
