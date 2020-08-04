import sys

def path_finder(x , y):

    """
    This function is find the path reversely.
    By using dynamic programming algorithm
    """
    # Base case (Early exit)
    if x == 1 and y == 1 + starting_value:
        return 0
    
    elif x == 1 + starting_value and y == 1:
        return 0

    # Normal case
    
    path_sum = 0

    # Find the path(x_cor)
    
    for i in range(1,10):
        # Range check
        if x - i >= 1:
            if data[x - i][y] == i:
                if data_store[x - i][y] == 0:
                    path_finder(x - i, y)
                path_sum += data_store[x - i][y]
        else:
            break

    # Find the path(y_cor)

    for i in range(1,10):
        # Range check
        if y - i >= 1:
            if data[x][y - i] == i:
                if data_store[x][y - i] == 0:
                    path_finder(x, y - i)
                path_sum += data_store[x][y - i]
        else:
            break

    # Store the data
    
    data_store[x][y] = path_sum
    return 0
            

# Data store (Setting the list)

n = int(input())

data = [0] * (n + 1) 
for i in range(1, n + 1):
    data[i] = [0] + list(map(int, sys.stdin.readline().split()))

data_store = []
for i in range(n + 1):
    data_store.append([0] * (n + 1))
starting_value = data[1][1]
data_store[1][1 + starting_value] = 1
data_store[1 + starting_value][1] = 1

# Call function
        
path_finder(n, n)

# Print the result

print(data_store[n][n])