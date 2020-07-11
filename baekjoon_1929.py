# Input value setting

num = input()
num_split = num.split()
for i in range(2):
    num_split[i] = int(num_split[i])

# First prime number checker(2~1000)

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
remove = []
result = []

# If number is multiply of prime number : erase

for i in range(2, 1001):
    for j in range(11):
        if i % prime[j] == 0:
            remove.append(i)

# Find prime number

for i in range(2, 1001):
    if i not in remove:
        result.append(i)

# Result

result = prime + result

# Calculate entire prime number until last input number

# Initial setting
data = []
for i in range(1, num_split[1]+1):
    data.append(i)


# Prime number check

for i in range(len(result)):
    k = 2
    while result[i] * k - 1 < num_split[1]:
        data[result[i] * k - 1] = None
        k += 1

# Total prime number result

final_result = []

for i in range(1, len(data)):
    if data[i] is not None:
        final_result.append(data[i])

# Find prime number that inside input values

check1 = 0
check2 = 0

for i in range(len(final_result)):
    if num_split[0] > final_result[i]:
        check1 = i+1
    elif final_result[i] <= num_split[1]:
        check2 = i
    else:
        break

result_final = final_result[check1:check2 + 1]
for i in range(len(result_final)):
    print(result_final[i])
