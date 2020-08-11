import sys

# Initial setting

data_store = [0] * 1001
data_store[0] = 1
data_store[1] = 1
n = int(input())

# Start with small value

l = 2

while l <= n:

    # Default setting (True)

    data = [True] * 1001

    # Erase impossible value

    k = 1
    while l - 2 * k >= 0:
        data[data_store[l - k] * 2 - data_store[l - 2 * k]] = False
        k += 1

    # Find the minimum value and save it 

    for i in range(1, 1002):
        if data[i] == True:
            data_store[l] = i
            break
        else:
            pass

    l += 1    

# Print result

print(data_store[n])