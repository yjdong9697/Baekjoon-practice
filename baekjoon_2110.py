import sys


def merge_sort(x):
    """
    This function is merger sort
    """
    len_list = len(x)
    mid = len_list // 2

    list_left = x[:mid]
    list_right = x[mid:]

    # Early exit

    if len_list == 1:
        return

    # Recursion

    merge_sort(list_left)
    merge_sort(list_right)

    # Concur

    left_count = 0
    right_count = 0
    global_count = 0

    while left_count < len(list_left) and right_count < len(list_right):
        if list_left[left_count] < list_right[right_count]:
            x[global_count] = list_left[left_count]
            left_count += 1
            global_count += 1

        else:
            x[global_count] = list_right[right_count]
            right_count += 1
            global_count += 1

    # If some list index surpass

    # left side surpass

    while right_count < len(list_right):
        x[global_count] = list_right[right_count]
        right_count += 1
        global_count += 1

    # right side surpass

    while left_count < len(list_left):
        x[global_count] = list_left[left_count]
        left_count += 1
        global_count += 1


# Initial setting (data input setting)

house_num, wifi_num = map(int, sys.stdin.readline().split())

data = []
for i in range(house_num):
    data.append(int(sys.stdin.readline()))

# Merge sort

merge_sort(data)

# Initial setting (Parametric search)

start = 0
end = 10e+9
result = []

while start <= end:

    # Define mid_value

    mid_value = (start + end) // 2

    # Count setting

    global_count = 0
    count = 1

    # Calculate how may interval is above mid_value
    # if below : mid_value is not minimum value (So find above value)

    for i in range(len(data)):
        if data[i] - data[global_count] >= mid_value:
            count += 1
            global_count = i

    if count >= wifi_num:
        result.append(mid_value)
        start = ((start + end) // 2) + 1

    elif count < wifi_num:
        end = ((start + end) // 2)

        # Final convergence (break point)

        if start == end:
            break

# Print result

print(int(max(result)))