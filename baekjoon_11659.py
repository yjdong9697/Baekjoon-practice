import sys

# Input value setting (using map function and sys module)

num, cal = map(int, sys.stdin.readline().split())

# list setting

data = list(map(int, sys.stdin.readline().split()))
sum_data_list = [0] * num
result_data = []

# Partition of sum calculation and find the result

for i in range(num):
    if i > 0 :
        sum_data_list[i] = sum_data_list[i-1] + data[i]
    elif i == 0:
        sum_data_list[i] = data[i]

for i in range(cal):
    start, end = map(int, sys.stdin.readline().split())
    if start == 1:
        result_data.append(sum_data_list[end - 1])
    else:
        result_data.append(sum_data_list[end-1]-sum_data_list[start - 2])

for i in range(cal):
    print(result_data[i])

