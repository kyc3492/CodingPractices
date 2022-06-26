n = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))
temp_operators = []
count_operators = 0
result = 0
max_result = 10000000001
min_result = -1 * 10000000001
isItStarted = False

def CALCULATOR(x, y, selector):
    if selector == 0:
        return x + y
    elif selector == 1:
        return x - y
    elif selector == 2:
        return x * y
    elif selector == 3:
        return int(x / y)
    else:
        pass

def SELECTOR():
    global result, isItStarted, max_result, min_result
    for i in range(4):
        if operators[i] != 0:
            temp_operators.append(i)
            operators[i] -= 1
            SELECTOR()
            if len(temp_operators) == len(nums) - 1:
                for c in range(len(temp_operators)):
                    if isItStarted == False:
                        result = CALCULATOR(nums[0], nums[1], temp_operators[0])
                        isItStarted = True
                    else:
                        result = CALCULATOR(result, nums[c + 1], temp_operators[c])
                
                if max_result > 10000000000:
                    max_result = result
                else:
                    max_result = max(max_result, result)

                if min_result < -1 * 10000000000:
                    min_result = result
                else:
                    min_result = min(min_result, result)
                
                result = 0
                isItStarted = False
            operators[i] += 1
            temp_operators.pop(len(temp_operators) - 1)

SELECTOR()
print(max_result)
print(min_result)