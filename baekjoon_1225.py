# Input value Setting

x = input()
x_split = x.split()

# Calculate sum

sum_1 = 0
sum_2 = 0

for i in range(len(x_split[0])):
    sum_1 += int(x_split[0][i])

for i in range(len(x_split[1])):
    sum_2 += int(x_split[1][i])

result = sum_1 * sum_2

# Print result

print(result)

