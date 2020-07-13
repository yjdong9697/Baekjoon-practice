def eratos(n):
    """
    This Function's return value is how many prime number less than n
    """

    # Definition of special case

    if n == 1:
        return 2

    # Setting base space

    num = list(range(0, n+1))

    # Setting starting base case

    next_num = 2

    # Until next_num**2 < n (using Eratosthenes method)

    while next_num**2 < n:
        for i in range(next_num*2, n+1, next_num):
            num[i] = 0
        initial = next_num + 1
        while True:
            if num[initial] != 0:
                next_num = num[initial]
                break
            else:
                initial += 1

    return num


# Input value

number = int(input())

# Make prime number list

result = eratos(7370000)


# Initial setting

count = 0

# Calculate and print the result

for i in range(2, len(result)):
    if result[i] != 0:
        count += 1
    if count == number:
        print(result[i])
        break

