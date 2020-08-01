import sys

# Recursion (Divide and conquer)

def split(data):
    """
    Checking all element is 1 or 0
    If not, divide it and find the result by recursion
    """

    len_of_data = len(data)
    one_checker = True
    zero_checker = True
    
    # Early exit 

    if len_of_data == 1:
        if data[0][0] == 1:
            return [1]
        else:
            return [0]

    # Check if all element is 1 or 0 

    for i in range(len_of_data):
        for j in range(len_of_data):
            if data[i][j] != 1:
                one_checker = False
            else:
                zero_checker = False

    # If all element is 1

    if one_checker == True:
        return [1]
    
    # If all element is 0
    
    elif zero_checker == True:
        return [0]
 
    # Else (Divide and conquer)
    
    elif one_checker != True and zero_checker != True:
        left_top = []
        right_top = []
        left_bottom = []
        right_bottom = []
        half_value = int(len_of_data / 2)

        for i in range(half_value):
            left_top.append(data[i][:half_value])
            right_top.append(data[i][half_value:])

        for i in range(half_value,len_of_data):
            left_bottom.append(data[i][:half_value])
            right_bottom.append(data[i][half_value:])

        return split(left_top) + split(right_top) + split(left_bottom) + split(right_bottom)

# Input value and data store

N = int(input())

data = []
for i in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

# Find the result and print it

result = split(data)
print(result.count(0))
print(result.count(1))