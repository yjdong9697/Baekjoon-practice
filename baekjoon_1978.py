def checker():
    """
    what is prime number in 100
    """

    # Initial prime number

    prime =[2,3,5,7,11,13,17,19,23,29,31]
    remove=[]
    result=[]

    # Find prime number below 1000

    for i in range(2,1000):
        for j in range(11):
            if i%prime[j] == 0:
                remove.append(i)
    for i in range(2,1000):
        if i not in remove:
            result.append(i)

    result = result + prime

    return result


# Find prime number

prime = checker()

# Input value

num = int(input())

# Calculate how many prime number

result_value = 0

x = input()
x_split = x.split()
for i in range(num):
    if int(x_split[i]) in prime:
        result_value += 1

# Print result

print(result_value)
