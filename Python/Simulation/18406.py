import sys
input = sys.stdin.readline

n = input()
n_array = []

sum_left = 0
sum_right = 0

for i in range(len(n) - 1):
    n_array.append(int(n[i]))
    #print(n_array)

for i in range(int(len(n_array) / 2)):
    sum_left += n_array[i]

for i in range(int(len(n_array) / 2)):
    #print(i)
    #print(len(n) - (i + 1))
    sum_right += n_array[len(n) - (i + 2)]

if sum_left == sum_right:
    print('LUCKY')
else:
    print('READY')