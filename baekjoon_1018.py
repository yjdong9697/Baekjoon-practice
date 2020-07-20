import sys

# Maximum = 42 * 42 * 64 < 2 * 10 ** 2 (Check all cases)

n, m = map(int, sys.stdin.readline().split())
data = []

# Setting the list

for k in range(n):
    data.append([0])

# Input data

for i in range(n):
    input_value = input()
    data[i] = list(input_value)

go_right_start = 0
go_down_start = 0
white_result = []


# start White cases (i,j is even or odd : White // else : Black)

while go_down_start + 7 <= n - 1:

    go_right_start_check = go_right_start % 2
    go_down_start_check = go_down_start % 2

    white_count = 0

    if go_right_start_check == go_down_start_check:
        for i in range(go_right_start, go_right_start + 8):
            for j in range(go_down_start, go_down_start + 8):
                if i % 2 == j % 2:
                    if data[j][i] == "B":
                        white_count += 1

                else:
                    if data[j][i] == "W":
                        white_count += 1

    else:
        for i in range(go_right_start, go_right_start + 8):
            for j in range(go_down_start, go_down_start + 8):
                if i % 2 == j % 2:
                    if data[j][i] == "W":
                        white_count += 1

                else:
                    if data[j][i] == "B":
                        white_count += 1

    white_result.append(white_count)

    if go_right_start + 7 < m - 1:
        go_right_start += 1

    else:
        go_right_start = 0
        go_down_start += 1

# Result (Black cases is symmetrically calculated)

minimum_value = min(white_result)
maximum_value = max(white_result)

final_result = min(minimum_value, 64 - maximum_value)

# Print result

print(final_result)
