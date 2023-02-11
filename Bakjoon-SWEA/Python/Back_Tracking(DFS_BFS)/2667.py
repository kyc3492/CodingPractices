# 0. 입력 준비
n = int(input())
# list comprehension으로 받은거까진 좋은데
# 받을 때부터 int 형으로 받을 순 없을까?
house_map = [list(map(int, input())) for _ in range(n)]

dc = [-1, 1, 0, 0]
dr = [0, 0, -1, 1]
total_list = []

# 2. 집 들어와서 DFS 탐색 진행
def house_finder(c, r):
    global count
    house_map[c][r] -= 1
    count += 1
    for d in range(4):
        nc = c + dc[d]
        nr = r + dr[d]
        if range_checker(nc, nr) and house_map[nc][nr] == 1:
            house_finder(nc, nr)
        
def range_checker(c, r):
    if 0 <= c < n and 0 <= r < n:
        return True
    else:
        return False

# 1. 전체 돌면서 집이 있으면 진행.
for c in range(n):
    for r in range(n):
        if house_map[c][r] == 1:
            count = 0
            house_finder(c, r)
            if count > 0:
                total_list.append(count)

total_list = sorted(total_list)
print(len(total_list))
for count in total_list:
    print(count)