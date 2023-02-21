from itertools import permutations

def solution(babbling):
    answer = 0
    available = ["aya", "ye", "woo", "ma"]
    words = []
    for i in range(1, 5):
        for j in permutations(available, i):
            words.append(''.join(j))
            
    for b in babbling:
        if b in words:
            answer += 1
                
    return answer