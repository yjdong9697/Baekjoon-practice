import sys
import copy

# Initial setting (num setting and stack setting)

num = int(sys.stdin.readline())
stack = [[0, 0], [0, 0], [0, 0]]

# Store only previous data (for using small data)

initial = 1
while initial <= num:
    if initial == 1:
        value1, value2, value3 = map(int, sys.stdin.readline().split())
        stack[0] = [value1, value1]
        stack[1] = [value2, value2]
        stack[2] = [value3, value3]

    else:
        value1, value2, value3 = map(int, sys.stdin.readline().split())
        stack_store = copy.deepcopy(stack)
        stack[0] = [min(stack_store[0][0], stack_store[1][0]) + value1,
                    max(stack_store[0][1], stack_store[1][1]) + value1]
        stack[1] = [min(stack_store[0][0], stack_store[1][0], stack_store[2][0]) + value2,
                    max(stack_store[0][1], stack_store[1][1], stack_store[2][1]) + value2]
        stack[2] = [min(stack_store[1][0], stack_store[2][0]) + value3,
                    max(stack_store[1][1], stack_store[2][1]) + value3]

    initial += 1

# Find max and min result

max_result = max(stack[0][1], stack[1][1], stack[2][1])
min_result = min(stack[0][0], stack[1][0], stack[2][0])

# Print result

print(max_result, min_result)