import sys

def recur(n):
    """
    This function is store the recurrence relation value
    If value is already exist in list = reuse it
    else: calculate it and store it
    """

    #  If not exist

    if recur_store[n - 1] == 0:
        recur(n - 1)
    
    result = 0
    for i in range(n):
        result += recur_store[i] * recur_store[n - 1 - i]

    recur_store[n] = result
        
    return


# Initial setting

n = int(input())

recur_store = [0] * (n + 1)
recur_store[0] = 1

recur(n)

# Print the result

print(recur_store[n])