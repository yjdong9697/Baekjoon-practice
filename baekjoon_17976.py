import sys

# Initial setting (Storing input value)

n = int(input())

thread_data = [0] * (n)
for i in range(n):
    thread_value = list(map(int, sys.stdin.readline().split()))
    thread_data[i] = thread_value

# Sorting the data

thread_data.sort()
thread_data = [0] + thread_data


# Recursion (case 1 : up case)
end_length = thread_data[n][0] + thread_data[n][1]
check_start = thread_data[1][0]
check_length = int((end_length - check_start) / (n - 1))
check_length_temp = check_length

thread_check_value = 1

length_min_store_case1 = []

while thread_check_value <= n - 2:
    if check_start + check_length <= thread_data[thread_check_value + 1][0]:
        check_start = thread_data[thread_check_value + 1][0]
        check_length = int((end_length - check_start) / (n - (thread_check_value + 1)))
        length_min_store_case1.append(check_length)
    
    elif thread_data[thread_check_value + 1][0] < check_start + check_length <= thread_data[thread_check_value + 1][0] + thread_data[thread_check_value + 1][1]:
        check_start += check_length
        check_length = int((end_length - check_start) / (n - (thread_check_value + 1)))
        length_min_store_case1.append(check_length)

    elif thread_data[thread_check_value + 1][0] + thread_data[thread_check_value + 1][1] < check_start + check_length:
        check_start = thread_data[thread_check_value + 1][0] + thread_data[thread_check_value + 1][1]
        check_length = int((end_length - check_start) / (n - (thread_check_value + 1)))
        length_min_store_case1.append(check_length)

    thread_check_value += 1

length_min_case1 = min(length_min_store_case1)

# Recursion (case 2 : down case)
check_length = check_length_temp 
thread_check_value = n
check_start = thread_data[n][0] + thread_data[n][1]

while thread_check_value >= 3:
    if check_start - check_length >= thread_data[thread_check_value - 1][0] + thread_data[thread_check_value -1][1]:
        check_start = thread_data[thread_check_value - 1][0] + thread_data[thread_check_value -1][1]
    
    elif thread_data[thread_check_value - 1][0] < check_start - check_length < thread_data[thread_check_value - 1][0] + thread_data[thread_check_value -1][1]:
        check_start = check_start - check_length

    elif check_start - check_length < thread_data[thread_check_value - 1][0]:
        if check_length > check_start - thread_data[thread_check_value - 1][0]:
            check_length = check_start - thread_data[thread_check_value - 1][0]
        check_start = thread_data[thread_check_value - 1][0]

    thread_check_value = thread_check_value - 1

# Final Check_length decision
if check_start - thread_data[1][0] < check_length_temp:
    check_length = check_start - thread_data[1][0]

length_min_data.append(check_length)


print(max(length_min_data))
