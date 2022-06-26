from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
city = []
house = []
chicken = []
for i in range(n):
    city.append(list(map(int, input().split())))
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        if city[i][j] == 2:
            chicken.append([i, j])

least_distance = -1
for survived in combinations(chicken, m):
    total_distance = 0
    #print(survived)
    for i in house:
        #print(i)
        distance = -1
        for j in range(m):
            r_house, c_house = map(int, i)
            r_survived, c_survived = map(int, survived[j])
            current_distance = abs(r_house - r_survived) + abs(c_house - c_survived)
            #print(current_distance)
            if distance == -1 or distance > current_distance:
                distance = current_distance
            #print(distance)
        total_distance += distance
        #print(total_distance)    
    if least_distance == -1 or least_distance > total_distance:
        least_distance = total_distance

print(least_distance)