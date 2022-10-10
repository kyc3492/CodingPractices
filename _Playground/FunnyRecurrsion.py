def Right_Solution(List):
    answer = 0

    def Recurrsion(List, MAX, current, idx):
        
        # 리스트를 다 돌면 회귀를 탈출합니다.
        if idx == len(List):
            # MAX와 비교합니다.
            # 예상대로라면 MAX = 12, current = 11로 12가 반환되어야 합니다.
            MAX = max(MAX, current)
            print("Depth :", idx, "NOW MAX :", MAX)
            return MAX
        else:
            for i in range(2):
                current += List[idx][i]
                # 핵심) 이전 회귀에서도 MAX를 유지해줍니다.
                print("Depth :", idx, "Before MAX :", MAX)
                MAX = Recurrsion(List, MAX, current, idx + 1)
                print("Depth :", idx, "After MAX :", MAX)
                ##################################
                current -= List[idx][i]
        return MAX

    answer = Recurrsion(List, 0, 0, 0)
    return answer

def Wrong_Solution(List):
    answer = 0

    def Recurrsion(List, MAX, current, idx):
        
        # 리스트를 다 돌면 회귀를 탈출합니다.
        if idx == len(List):
            # MAX와 비교합니다.
            # 예상대로라면 MAX = 12, current = 11로 12가 반환되어야 합니다.
            MAX = max(MAX, current)
            print("Depth :", idx, "NOW MAX :", MAX)
            return MAX
        else:
            for i in range(2):
                current += List[idx][i]
                print("Depth :", idx, "Before MAX :", MAX)
                Recurrsion(List, MAX, current, idx + 1)
                print("Depth :", idx, "After MAX :", MAX)
                current -= List[idx][i]
        return MAX

    answer = Recurrsion(List, 0, 0, 0)
    return answer

List = [[1, 2],
        [3, 4],
        [6, 5]]

print("Result of Wrong_Solution ->", Wrong_Solution(List))
print("##############################################")
print("Result of Right_Solution ->", Right_Solution(List))