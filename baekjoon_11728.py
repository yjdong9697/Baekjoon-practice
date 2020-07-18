# Size input

size = input()
size_split = size.split()

a_size = int(size_split[0])
b_size = int(size_split[1])

# a input and make list

a = input()
a_split = a.split()

# b input and make list

b = input()
b_split = b.split()

# concat two list

result = []
i = 0
j = 0


# lower case : append

while (i <= a_size - 1) and (j <= b_size - 1):
    if int(a_split[i]) >= int(b_split[j]):
        result.append(b_split[j])

        # If end case

        if b_size - 1 == j:
            for v in range(i, len(a_split[i:])+i):
                result.append(a_split[v])
            break

        else:
            j += 1

    elif int(a_split[i]) < int(b_split[j]):
        result.append(a_split[i])

        # If end case

        if len(a_split) - 1 == i:
            for v in range(j, len(b_split[j:])+j):
                result.append(b_split[v])
            break

        else:
            i += 1

# Print result

for i in range(len(result)-1):
    print(result[i], end=" ")
print(result[-1])