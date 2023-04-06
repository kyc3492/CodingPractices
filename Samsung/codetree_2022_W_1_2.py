from collections import defaultdict

# 초기 값 지정
n, m = -1, -1
MAX_M = 10
# 이중 연결리스트의 초기화 -> head, tail, prev, next
# 벨트는 최대 10개, idx대로 1~10
head = [0 for _ in range(MAX_M + 1)]
tail = [0 for _ in range(MAX_M + 1)]
# 물건은 ID: Weight 모양의 dict를 만들자.
weight = {}
# prev, next 역시 dict를 만들면 된다.
# lambda 식으로 defaultdict를 만들어주면 순회 돌면서 찾는 속도를 줄일 수 있음.
# 초기값은 0으로 주면서 0인 경우 없다는 느낌으로
prev = defaultdict(lambda: 0)
next = defaultdict(lambda: 0)
# 물건 id 별 벨트 번호를 기록할 것임.
# -1은 사라진 물건.
belt_num = defaultdict(lambda: -1)
# 벨트의 고장 여부를 파악할 거임.
# True인 경우에는 고장난 것.
broken = [False] * MAX_M

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

# ID에 해당하는 상자 삭제
def remove_id(box_id, remove_belt):
    # 박스에 할당된 벨트 번호 제거
    b_num = belt_num[box_id]
    # 벨트에서 내려야하는 상황이면
    if remove_belt:
        belt_num[box_id] = -1

    # 하나 남아있었다면 head, tail이 사라짐
    if head[b_num] == tail[b_num]:
        head[b_num] = tail[b_num] = 0

    # head가 삭제된다면 head만 변경
    elif box_id == head[b_num]:
        next_id = next[box_id]
        head[b_num] = next_id
        prev[next_id] = 0

    # tail이 삭제된다면 tail만 변경
    elif box_id == tail[b_num]:
        prev_id = prev[box_id]
        tail[b_num] = prev_id
        next[box_id] = 0

    # 중간이 삭제된다면 수선
    else:
        prev_id, next_id = prev[box_id], next[box_id]
        next[prev_id] = next_id
        prev[next_id] = prev_id

    # next, prev 삭제
    next[box_id] = prev[box_id] = 0


# target_id를 받으면 바로 뒤에 id를 추가
def push_id(target, box_id):
    next[target] = box_id
    prev[box_id] = target

    # target이 tail이었다면 tail을 변경
    b_num = belt_num[target]
    if tail[b_num] == target:
        tail[b_num] = box_id


# 상자 하차
def load_boxes(command):
    w_max = command[1]
    loaded = 0

    # 컨베이어벨트들을 확인
    for belt_idx in range(1, m + 1):
        # 고장난 건 패스
        if broken[belt_idx]:
            continue
        # 각 벨트들의 head를 본다. 비어있는 것들 패스
        if head[belt_idx] != 0:
            box_id = head[belt_idx]
            # 이 head가 w_max 이하라면
            if weight[box_id] <= w_max:
                # 하차 무게에 더하고
                loaded += weight[box_id]
                # head를 넘겨줘야함. + 해당 벨트에서 내리자
                remove_id(box_id, True)
            # head를 맨 뒤로 넘겨야 하는 상황이라면
            elif next[box_id] != 0:
                # 제거해주고, 단 벨트에서 내리는 건 아님.
                remove_id(box_id, False)
                # 맨 뒤에 push
                push_id(tail[belt_idx], box_id)

    print(loaded)
    return


# 상자 제거
def remove_box(command):
    r_id = command[1]

    if belt_num[r_id] == -1:
        print(-1)
        return

    # 상자 제거
    remove_id(r_id, True)
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

        #prev[f_id] = 0
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
                push_id(tail[belt_idx], head[belt_idx])
                # tail 변경
                tail[belt_idx] = tail[b_num]

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
