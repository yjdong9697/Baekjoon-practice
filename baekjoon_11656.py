# Input value

x = input()

# Initial setting

result = []

# Make word and append result list

for i in range(len(x)):
    result.append(x[i:])


# Sorting

result.sort()

# Print result

for i in range(len(result)):
    print(result[i])
